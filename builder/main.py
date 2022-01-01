"""The main module of build resources program."""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from filecmp import cmpfiles
from importlib import resources
from pathlib import Path
from tempfile import NamedTemporaryFile

from PySide6.scripts.pyside_tool import rcc  # type: ignore

from builder.color import RGBA
from qdarktheme.util import get_qdarktheme_root_path, multi_replace

DIST_DIR_PATH = get_qdarktheme_root_path() / "dist"


@dataclass(unsafe_hash=True, frozen=True)
class _Url:
    """Class handling the properties of the $url{...} variable in the stylesheet template."""

    icon: str
    color_id: str
    rotate: str
    match_text: str
    file_name: str


def _remove_comment(stylesheet: str) -> str:
    """Remove comment from the stylesheet string."""
    comment_pattern = re.compile(r" */\*[\s\S]*?\*/")
    match = comment_pattern.search(stylesheet)
    license_text = "/* MIT License */" if match is None else match.group()
    # Remove qss comment
    stylesheet = comment_pattern.sub("", stylesheet)
    # Change blank lines to one blank line
    stylesheet = re.sub(r"\n\s*\n", "\n", stylesheet)

    return license_text + stylesheet


def _parse_url(stylesheet: str) -> set[_Url]:
    """Parse $url{...} symbol in template stylesheet."""
    urls = set()
    for match in re.finditer(r"\$url\{.+\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$url", "")

        url_property: dict[str, str] = json.loads(json_text)
        icon = url_property["icon"]
        color_id = url_property["id"]
        rotate = url_property.get("rotate", "0")

        file_name = f"{icon.replace('.svg', '')}__{color_id}__rotate-{rotate}.svg"
        urls.add(_Url(icon, color_id, rotate, match_text, file_name))
    return urls


def _build_init_file(theme: str, output_dir_path: Path) -> None:
    contents = f'"""Package containing the resources for {theme} theme."""\n'
    (output_dir_path / "__init__.py").write_text(contents)


def _build_svg_file(urls: set[_Url], colors: dict[str, RGBA], svg_dir_path: Path, output_dir_path: Path) -> None:
    svg_codes: dict[str, str] = {}  # {file name: svg code}
    output_dir_path.mkdir(exist_ok=True)
    svg_paths = [path for path in svg_dir_path.iterdir() if ".svg" in path.name]
    svg_codes = {path.name: path.read_text(encoding="utf-8") for path in svg_paths}

    # QSvg does not support #RRGGBBAA. Therefore, we need to set the alpha value to `fill-opacity` instead.
    def to_svg_color_format(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f'fill="rgb({r}, {g}, {b})" fill-opacity="{a}"'

    for url in urls:
        rgba = colors[url.color_id]
        # Change color and rotate. See https://stackoverflow.com/a/15139069/13452582
        new_contents = f'{to_svg_color_format(rgba)} transform="rotate({url.rotate}, 12, 12)"'
        svg_code_converted = svg_codes[url.icon].replace('fill="#FFFFFF"', new_contents)
        with (output_dir_path / url.file_name).open("w") as f:
            f.write(svg_code_converted)


def _build_palette_file(colors: dict[str, RGBA], output_dir_path: Path, palette_template: str) -> None:
    def to_arg_text(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f"{r}, {g}, {b}, {a*255}"

    replacements = {f'"${color_id}"': to_arg_text(rgba) for color_id, rgba in colors.items()}
    with (output_dir_path / "palette.py").open("w") as f:
        f.write(multi_replace(palette_template, replacements))


def _build_template_stylesheet(
    theme: str, stylesheet: str, urls: set[_Url], colors: dict[str, RGBA], output_dir_path: Path
) -> None:
    url_replacements = {url.match_text: f"url(${{path}}/dist/{theme}/svg/{url.file_name})" for url in urls}
    colors_converted = {f"${color_id}": str(rgba) for color_id, rgba in colors.items()}
    template_stylesheet = multi_replace(stylesheet, {**url_replacements, **colors_converted})
    with (output_dir_path / "stylesheet.py").open("w") as f:
        f.write(f'"""Contents that define stylesheet for {theme} theme."""\n\n')
        f.write(f'STYLE_SHEET = """\n{template_stylesheet}\n"""\n')


def _generate_qt_resource_file(svg_dir_path: Path, output_dir_path: Path, theme: str) -> None:
    qrc = f'<RCC version="1.0"><qresource prefix="qdarktheme/dist/{theme}">'
    for file in svg_dir_path.iterdir():
        qrc += f"<file>{svg_dir_path.name}/{file.name}</file>"
    qrc += "</qresource></RCC>"

    with NamedTemporaryFile(suffix=".qrc", dir=str(output_dir_path)) as f:
        qrc_file_path = output_dir_path / f.name
        qrc_file_path.write_text(qrc, "utf-8")
        py_resource_file_path = output_dir_path / "rc_icons.py"

        # Patch PySide6.scripts.pyside_tool
        temp_argv, temp_exit = sys.argv.copy(), sys.exit
        sys.argv[1:] = [str(qrc_file_path), "-o", str(py_resource_file_path)]
        # Not finish program with sys.exit()
        sys.exit = lambda _: "dummy"
        rcc()
        # Remove patch
        sys.argv, sys.exit = temp_argv, temp_exit

    resource_code = py_resource_file_path.read_text().replace("PySide6", "qdarktheme.qtpy")
    result1 = re.search(r"QtCore\.qRegisterResourceData\(.+\)", resource_code)
    result2 = re.search(r"QtCore\.qUnregisterResourceData\(.+\)", resource_code)
    if result1 is None or result2 is None:
        raise RuntimeError(
            f"""
            Cannot find QtCore.qRegisterResourceData() or QtCore.qUnregisterResourceData() in {py_resource_file_path}
            """
        )
    resource_code = resource_code.replace(result1.group(), f"{result1.group()}  # type: ignore")
    resource_code = resource_code.replace(result2.group(), f"{result2.group()}  # type: ignore")
    resource_code = '"""Module for qt resources system."""\n' + resource_code
    py_resource_file_path.write_text(resource_code)


def _generate_root_init_file(output_dir_path: Path, themes: list[str], doc_string: str = "", source: str = "") -> None:
    with (output_dir_path / "__init__.py").open("w") as f:
        if len(doc_string) != 0:
            f.write(doc_string + "\n")
        f.write(f"THEMES = {themes}\n".replace("'", '"').replace("[", "(").replace("]", ")"))
        if len(source) != 0:
            f.write(source + "\n")


def build_resources(build_path: Path, theme_file_paths: list[Path], root_init_file_doc: str) -> None:
    """Build resources for qdarktheme module."""
    stylesheet = _remove_comment(resources.read_text("builder", "base.qss"))
    urls = _parse_url(stylesheet)
    palette_template = resources.read_text("builder", "palette.template.py")
    svg_dir_path = Path(__file__).parent / "svg"
    themes = []

    for theme_file_path in theme_file_paths:
        theme = theme_file_path.stem
        themes.append(theme)
        output_dir_path = build_path / theme
        output_dir_path.mkdir()

        hex_colors = json.loads(theme_file_path.read_bytes())
        rgba_colors = {color_id: RGBA.from_hex(color_hex) for color_id, color_hex in hex_colors.items()}

        _build_init_file(theme, output_dir_path)
        _build_svg_file(urls, rgba_colors, svg_dir_path, output_dir_path / "svg")
        _build_palette_file(rgba_colors, output_dir_path, palette_template)
        _build_template_stylesheet(theme, stylesheet, urls, rgba_colors, output_dir_path)
        _generate_qt_resource_file(output_dir_path / "svg", output_dir_path, theme)

    _generate_root_init_file(build_path, themes, root_init_file_doc)


def compare_all_files(dir1: Path, dir2: Path) -> list[str]:
    """Check if the contents of the files with the same name in the two directories are the same.

    Args:
        dir1: The directory containing files.
        dir2: The directory containing files.

    Returns:
        list[str]: A list of file names with different contents。
    """
    target_files = set()
    for file in dir2.glob("**/*"):
        if not file.is_file():
            continue
        target_files.add(str(file).replace(str(dir2), "")[1:])
    _, mismatch, err = cmpfiles(dir1, dir2, target_files)
    files_changed = mismatch + err
    if not [file for file in files_changed if "rc_icons.py" not in file]:
        return []
    return [str(Path(dir1).relative_to(Path.cwd()) / file) for file in files_changed]
