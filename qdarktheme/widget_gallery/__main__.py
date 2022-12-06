"""Module allowing for `python -m qdarktheme.widget_gallery`."""
import sys

import qdarktheme
from qdarktheme.qtpy.QtWidgets import QApplication
from qdarktheme.widget_gallery.main_window import WidgetGallery

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_style()
    win = WidgetGallery()
    win.show()
    app.exec()
