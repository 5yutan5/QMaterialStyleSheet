"""Contents that define stylesheet for light theme."""

STYLE_SHEET = """
* {
    padding: 0;
    margin: 0;
    border: none;
    border-style: none;
    border-image: unset;
    outline: none;
}
QToolBar * {
    margin: 0;
    padding: 0;
}
QWidget {
    background: #f8f9fa;
    color: #4d5157;
    selection-background-color: #0081db;
    selection-color: #f8f9fa;
}
QWidget:disabled {
    color: #babdc2;
    selection-background-color: #dadce0;
    selection-color: #babdc2;
}
QWidget {
    backward-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
    forward-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
    leftarrow-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
    rightarrow-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
    dialog-ok-icon: url(${path}/themes/light/svg/check__icon-foreground.svg);
    dialog-cancel-icon: url(${path}/themes/light/svg/close__icon-foreground.svg);
    dialog-yes-icon: url(${path}/themes/light/svg/check_circle__icon-foreground.svg);
    dialog-no-icon: url(${path}/themes/light/svg/cancel__icon-foreground.svg);
    dialog-apply-icon: url(${path}/themes/light/svg/check__icon-foreground.svg);
    dialog-reset-icon: url(${path}/themes/light/svg/restart_alt__icon-foreground.svg);
    dialog-save-icon: url(${path}/themes/light/svg/save__icon-foreground.svg);
    dialog-discard-icon: url(${path}/themes/light/svg/delete__icon-foreground.svg);
    dialog-close-icon: url(${path}/themes/light/svg/close__icon-foreground.svg);
    dialog-open-icon: url(${path}/themes/light/svg/folder_open__icon-foreground.svg);
    dialog-help-icon: url(${path}/themes/light/svg/help__icon-foreground.svg);
    filedialog-parent-directory-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground.svg);
    filedialog-new-directory-icon: url(${path}/themes/light/svg/create_new_folder__icon-foreground.svg);
    titlebar-close-icon: url(${path}/themes/light/svg/close__icon-foreground.svg);
    titlebar-normal-icon: url(${path}/themes/light/svg/flip_to_front__icon-foreground.svg);
}
QCommandLinkButton {
    qproperty-icon: url(${path}/themes/light/svg/east__highlight.svg);
}
QMainWindow::separator {
    width: 4px;
    height: 4px;
    background: #dadce0;
}
QMainWindow::separator:hover,
QMainWindow::separator:pressed {
    background: #0081db;
}
QToolTip {
    background: #ffffff;
    color: #4d5157;
    border: 1px solid #dadce0;
}
QSizeGrip {
    width: 0;
    height: 0;
    image: none;
}
QStatusBar {
    background: #dfe1e5;
}
QStatusBar QWidget {
    background: transparent;
    padding: 3px;
    border-radius: 4px;
}
QStatusBar QWidget:hover {
    background: #d1d4da;
}
QStatusBar QWidget:pressed {
    background: #c3c7ce;
}
QStatusBar QWidget:disabled {
    background: #edeef0;
}
QStatusBar QWidget:checked {
    background: #c3c7ce;
}
QCheckBox,
QRadioButton {
    border-top: 2px solid transparent;
    border-bottom: 2px solid transparent;
}
QCheckBox:!window,
QRadioButton:!window {
    background: transparent;
}
QCheckBox:hover,
QRadioButton:hover {
    border-bottom: 2px solid #0081db;
}
QGroupBox {
    font-weight: bold;
    border: 1px solid #dadce0;
    border-radius: 4px;
    padding: 2px;
    margin: 9px 0 4px 0;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 7px;
    top: 2px;
    margin: 0 2px;
}
QGroupBox:flat {
    border-color: transparent;
    padding: 2px 0 0 0;
}
QMenuBar {
    background: #f8f9fa;
    padding: 2px;
    border-bottom: 1px solid #dadce0;
}
QMenuBar::item {
    background: transparent;
    padding: 4px;
}
QMenuBar::item:selected {
    padding: 4px;
    background: #dadce0;
    border-radius: 4px;
}
QMenuBar::item:pressed {
    padding: 4px;
    margin-bottom: 0;
    padding-bottom: 0;
}
QToolBar {
    background: #ebebeb;
    padding: 1px;
    font-weight: bold;
    spacing: 2px;
    margin: 1px;
}
QToolBar::handle:horizontal {
    width: 20px;
    image: url(${path}/themes/light/svg/drag_indicator_horizontal__icon-foreground.svg);
}
QToolBar::handle:vertical {
    height: 20px;
    image: url(${path}/themes/light/svg/drag_indicator_horizontal__icon-foreground__rotate-90.svg);
}
QToolBar::separator {
    background: #dadce0;
}
QToolBar::separator:horizontal {
    width: 2px;
    margin: 0 6px;
}
QToolBar::separator:vertical {
    height: 2px;
    margin: 6px 0;
}
QToolBar > QToolButton {
    background: transparent;
    padding: 3px;
    border-radius: 4px;
}
QToolBar > QToolButton:hover {
    background: #d7d7d7;
}
QToolBar > QToolButton:pressed {
    background: #c4c4c4;
}
QToolBar > QToolButton:checked {
    background: #c4c4c4;
}
QToolBar > QToolButton#qt_toolbar_ext_button {
    image: url(${path}/themes/light/svg/double_arrow__icon-foreground.svg);
}
QToolBar > QToolButton#qt_toolbar_ext_button:disabled {
    image: url(${path}/themes/light/svg/double_arrow__icon-foreground-disabled.svg);
}
QToolBar > QWidget {
    background: transparent;
}
QMenu {
    background: #ffffff;
    padding: 8px 0;
    border: 1px solid #dadce0;
}
QMenu::separator {
    height: 1px;
    background: #dadce0;
}
QMenu::item {
    padding: 4px 28px;
}
QMenu::item:selected {
    background: #dadce0;
}
QMenu::icon {
    padding-left: 10px;
    width: 14px;
    height: 14px;
}
QMenu::right-arrow {
    margin: 2px;
    padding-left: 12px;
    height: 20px;
    width: 20px;
    image: url(${path}/themes/light/svg/chevron_right__icon-foreground.svg);
}
QMenu::right-arrow:disabled {
    image: url(${path}/themes/light/svg/chevron_right__icon-foreground-disabled.svg);
}
QScrollBar {
    background: transparent;
}
QScrollBar:horizontal {
    height: 7px;
}
QScrollBar:vertical {
    width: 7px;
}
QScrollBar::handle {
    background: rgba(155.000, 155.000, 157.000, 0.737);
    border-radius: 3px;
}
QScrollBar::handle:hover {
    background: rgba(117.000, 117.000, 119.000, 0.827);
}
QScrollBar::handle:pressed {
    background: rgba(96.000, 96.000, 98.000, 0.933);
}
QScrollBar::handle:horizontal {
    min-width: 8px;
}
QScrollBar::handle:vertical {
    min-height: 8px;
}
QScrollBar::sub-line, QScrollBar::add-line {
    width: 0;
    height: 0;
}
QScrollBar::sub-page, QScrollBar::add-page {
    background: transparent;
}
QProgressBar {
    border: 1px solid #dadce0;
    border-radius: 4px;
    text-align: center;
    color: #4d5157;
}
QProgressBar::chunk {
    background: #0081db;
    border-radius: 3px;
}
QProgressBar::chunk:disabled {
    background: #dadce0;
}
QPushButton {
    border: 1px solid #dadce0;
    padding: 4px 8px;
    border-radius: 4px;
    color: #0081db;
}
QPushButton:hover,
QPushButton:flat:hover {
    background: #e2eafb;
}
QPushButton:pressed,
QPushButton:flat:pressed {
    background: #b5caf4;
}
QPushButton:checked,
QPushButton:flat:checked {
    border-color: #0081db;
}
QPushButton:disabled,
QPushButton:flat:checked {
    border-color: #dadce0;
}
QPushButton:flat {
    background: transparent;
    border-color: transparent;
}
QDialogButtonBox QPushButton {
    min-width: 65px;
}
QToolButton {
    background: transparent;
    padding: 5px;
    border-radius: 2px;
    spacing: 2px;
}
QToolButton:hover {
    background: #e2eafb;
}
QToolButton:pressed {
    background: #b5caf4;
}
QToolButton:selected,
QToolButton:checked {
    background: #b5caf4;
}
QToolButton::checked:disabled {
    background: #dadce0;
}
QToolButton::menu-indicator {
    height: 18px;
    width: 18px;
    top: 6px;
    left: 3px;
    image: url(${path}/themes/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QToolButton::menu-indicator:disabled {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QToolButton::menu-arrow {
    height: 8px;
    width: 8px;
}
QToolButton[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "popupMode=MenuButtonPopup"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "popupMode=\\\"1\\\""}
$env_patch{"version": ">=6.0.0", "value": "popupMode=MenuButtonPopup"}
] {
    padding-right: 14px;
}
QToolButton[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "popupMode=MenuButtonPopup"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "popupMode=\\\"1\\\""}
$env_patch{"version": ">=6.0.0", "value": "popupMode=MenuButtonPopup"}
]::menu-button {
    border: none;
    border-radius: 4px;
    width: 18px;
    image: url(${path}/themes/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QToolButton[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "popupMode=MenuButtonPopup"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "popupMode=\\\"1\\\""}
$env_patch{"version": ">=6.0.0", "value": "popupMode=MenuButtonPopup"}
]::menu-button:disabled {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QComboBox {
    border: 1px solid #dadce0;
    border-radius: 4px;
    min-height: 1.5em;
    padding: 0 4px;
    background: #f8f9fa;
}
QComboBox:focus,
QComboBox:open {
    border: 1px solid #0081db;
}
QComboBox::drop-down {
    subcontrol-position: center right;
    border: none;
    padding-right: 4px;
}
QComboBox::down-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/themes/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QComboBox::down-arrow:disabled {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QComboBox::item:selected {
    border: none;
    background: #4ca6e5;
    color: #4d5157;
}
QComboBox QAbstractItemView {
    background: #ffffff;
    margin: 0;
    border: 1px solid #dadce0;
    selection-background-color: #4ca6e5;
    selection-color: #4d5157;
    padding: 2px;
}
QComboBox QAbstractItemView[
$env_patch{"version": "<6.0.0", "value": "frameShape=\\\"0\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=NoFrame"}
] {
    border-color: #dadce0;
}
QSlider {
    padding: 2px 0;
}
QSlider::groove {
    border-radius: 2px;
}
QSlider::groove:horizontal {
    height: 4px;
}
QSlider::groove:vertical {
    width: 4px;
}
QSlider::sub-page, QSlider::handle {
    background: #0081db;
}
QSlider::sub-page:disabled,
QSlider::add-page:disabled,
QSlider::handle:disabled {
    background: #dadce0;
}
QSlider::add-page {
    background: #dadce0;
}
QSlider::handle:hover {
    background: #7fa6e4;
}
QSlider::handle:horizontal {
    width: 16px;
    height: 8px;
    margin: -6px 0;
    border-radius: 8px;
}
QSlider::handle:vertical {
    width: 8px;
    height: 16px;
    margin: 0 -6px;
    border-radius: 8px;
}
QTabWidget::pane {
    border: 1px solid #dadce0;
    border-radius: 3px;
}
QTabBar {
    qproperty-drawBase: 0;
}
QTabBar::close-button:selected {
    image: url(${path}/themes/light/svg/close__icon-foreground.svg);
}
QTabBar::close-button:!selected {
    image: url(${path}/themes/light/svg/close__tabbar-button-inselected.svg)
}
QTabBar::close-button:disabled {
    image: url(${path}/themes/light/svg/close__icon-foreground-disabled.svg);
}
QTabBar::close-button:hover {
    background: #93b2ef;
    border-radius: 4px
}
QTabBar::close-button:hover:!selected {
    background: #aec5f4;
}
QTabBar::tab {
    padding: 3px;
}
QTabBar::tab:hover {
    background: #e2eafb;
}
QTabBar::tab:selected {
    color: #0081db;
    background: #b5caf4;
}
QTabBar::tab:selected:disabled {
    background: #dadce0;
    color: #babdc2;
}
QTabBar::tab:top {
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
    border-bottom: 2px solid #dadce0;
    margin-left: 4px;
}
QTabBar::tab:top:selected {
    border-bottom: 2px solid #0081db;
}
QTabBar::tab:top:hover {
    border-color: #0081db;
}
QTabBar::tab:top:selected:disabled {
    border-color: #dadce0;
}
QTabBar::tab:bottom {
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    border-top: 2px solid #dadce0;
    margin-left: 4px;
}
QTabBar::tab:bottom:selected {
    border-top: 2px solid #0081db;
}
QTabBar::tab:bottom:hover {
    border-color: #0081db;
}
QTabBar::tab:bottom:selected:disabled {
    border-color: #dadce0;
}
QTabBar::tab:left {
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
    border-right: 2px solid #dadce0;
    margin-top: 4px;
}
QTabBar::tab:left:selected {
    border-right: 2px solid #0081db;
}
QTabBar::tab:left:hover {
    border-color: #0081db;
}
QTabBar::tab:left:selected:disabled {
    border-color: #dadce0;
}
QTabBar::tab:right {
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    border-left: 2px solid #dadce0;
    margin-top: 4px;
}
QTabBar::tab:right:selected {
    border-left: 2px solid #0081db;
}
QTabBar::tab:right:hover {
    border-color: #0081db;
}
QTabBar::tab:right:selected:disabled {
    border-color: #dadce0;
}
QDockWidget {
    border: 1px solid #dadce0;
    border-radius: 4px;
}
QDockWidget::title {
    padding: 3px;
    spacing: 4px;
    background: #edeef0;
}
QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background: #e2eafb;
    border-radius: 2px;
}
QFrame {
    border: 1px solid #dadce0;
    padding: 1px;
    border-radius: 4px;
}
.QFrame {
    padding: 0;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=NoFrame"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"0\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=NoFrame"}
] {
    border-color: transparent;
    padding: 0;
}
.QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=NoFrame"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"0\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=NoFrame"}
] {
    border: none;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=Panel"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"2\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=Panel"}
] {
    border-color: #e1e5ea;
    background: #e1e5ea;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=HLine"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"4\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=HLine"}
] {
    max-height: 2px;
    border: none;
    background: #dadce0;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=VLine"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"5\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=VLine"}
] {
    max-width: 2px;
    border: none;
    background: #dadce0;
}
QLCDNumber {
    color: #4d5157;
    min-width: 2em;
    margin: 2px;
}
QToolBox:selected {
    border: 2px solid #0081db;
}
QToolBox::tab {
    background: #edeef0;
    border-bottom: 2px solid #dadce0;
}
QToolBox::tab:selected {
    border-bottom: 2px solid #0081db;
}
QToolBox::tab:selected:disabled {
    border-bottom: 2px solid #dadce0;
}
QSplitter::handle {
    background: #dadce0;
    margin: 1px 3px;
}
QSplitter::handle:hover {
    background: #0081db;
}
QSplitter::handle:horizontal {
    width: 5px;
    image: url(${path}/themes/light/svg/horizontal_rule__icon-foreground__rotate-90.svg);
}
QSplitter::handle:horizontal:disabled {
    image: url(${path}/themes/light/svg/horizontal_rule__icon-foreground-disabled__rotate-90.svg);
}
QSplitter::handle:vertical {
    height: 5px;
    image: url(${path}/themes/light/svg/horizontal_rule__icon-foreground.svg);
}
QSplitter::handle:vertical:disabled {
    image: url(${path}/themes/light/svg/horizontal_rule__icon-foreground-disabled.svg);
}
QSplitterHandle::item:hover {}
QAbstractScrollArea {
    selection-background-color: #4ca6e5;
    selection-color: #4d5157;
    margin: 1px;
}
QAbstractScrollArea:disabled {
    selection-background-color: #0081db;
}
QAbstractScrollArea > .QWidget {
    background: transparent;
}
QAbstractScrollArea > .QWidget > .QWidget {
    background: transparent;
}
QTextEdit, QPlainTextEdit {
    background: #ffffff;
}
QTextEdit:focus,
QTextEdit:selected,
QPlainTextEdit:focus,
QPlainTextEdit:selected {
    border: 1px solid #0081db;
    selection-background-color: #a2d8ff;
}
QTextEdit:!focus,
QPlainTextEdit:!focus {
    $env_patch{"version": ">=5.15.0", "value": "selection-background-color: #e4e6f2"};
}
QTextEdit:!active,
QPlainTextEdit:!active {
    $env_patch{"version": "<5.15.0", "value": "selection-background-color: #e4e6f2"};
}
QAbstractItemView {
    alternate-background-color: #e9ecef;
}
QAbstractItemView::item {
    spacing: 6px;
    $env_patch{"version": ">=6.0.0", "value": "border-color: transparent"};
}
QAbstractItemView:selected:!active,
QAbstractItemView:selected:!focus,
QAbstractItemView::item:selected:!active,
QTreeView::branch:selected:!active {
    background: #e4e6f2;
}
QAbstractItemView::item:selected,
QTreeView::branch:selected {
    background: #4ca6e5;
    color: #4d5157;
}
QAbstractItemView::item:!selected:hover,
QTreeView::branch:!selected:hover {
    background: #d3d3d3;
}
QAbstractItemView::item:selected:disabled {
    color: #babdc2;
}
QAbstractItemView QLineEdit,
QAbstractItemView QAbstractSpinBox,
QAbstractItemView QComboBox,
QAbstractItemView QAbstractButton {
    padding: 0;
    margin: 1px;
}
QTreeView::branch {
    border-image: url(${path}/themes/light/svg/vertical_line__guides-stroke-inactive.svg) 0;
}
QTreeView::branch:active {
    border-image: url(${path}/themes/light/svg/vertical_line__icon-foreground.svg) 0;
}
QTreeView::branch:disabled {
    border-image: url(${path}/themes/light/svg/vertical_line__icon-foreground-disabled.svg) 0;
}
QTreeView::branch:has-siblings:adjoins-item,
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: unset;
}
QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: unset;
    image: url(${path}/themes/light/svg/chevron_right__icon-foreground.svg);
}
QTreeView::branch:has-children:!has-siblings:closed:disabled,
QTreeView::branch:closed:has-children:has-siblings:disabled {
    image: url(${path}/themes/light/svg/chevron_right__icon-foreground-disabled.svg);
}
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    border-image: unset;
    image: url(${path}/themes/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QTreeView::branch:open:has-children:!has-siblings:disabled,
QTreeView::branch:open:has-children:has-siblings:disabled  {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QTableView {
    gridline-color: #58595c;
    background: #ffffff;
}
QTableView QTableCornerButton::section {
    border-top-left-radius: 2px;
    background: #dadce0;
}
QTableView QTableCornerButton::section:pressed {
    background: #4ca6e5;
}
QTableView > QHeaderView{
    background: #ffffff;
}
QTableView > QHeaderView::section:horizontal:first {
    margin-left: 1px;
}
QTableView > QHeaderView::section:vertical:first {
    margin-top: 1px;
}
QHeaderView {
    padding: 0;
    margin: 0;
    border: none;
    border-radius: 0;
}
QHeaderView::section {
    background: #dadce0;
    text-align: left;
    padding: 0 4px;
    border: none;
}
QHeaderView::section:horizontal:on,
QHeaderView::section:vertical:on {
    border-color: #0081db;
}
QHeaderView::section:horizontal:on:disabled,
QHeaderView::section:vertical:on:disabled {
    color: #dadce0;
    border-color: #dadce0;
}
QHeaderView::section:horizontal {
    border-top: 2px solid transparent;
    margin-right: 1px;
}
QHeaderView::section:vertical {
    border-left: 2px solid transparent;
    margin-bottom: 1px;
}
QHeaderView::section::last,
QHeaderView::section::only-one {
    margin: 0;
}
QHeaderView::down-arrow {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QHeaderView::down-arrow:disabled {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QHeaderView::up-arrow {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground.svg);
}
QHeaderView::up-arrow:disabled {
    image: url(${path}/themes/light/svg/expand_less__icon-foreground-disabled.svg);
}
QHeaderView::down-arrow::horizontal,
QHeaderView::up-arrow::horizontal {
    width: 20px;
    padding-right: 2px;
}
QHeaderView::down-arrow::vertical,
QHeaderView::up-arrow::vertical {
    height: 0;
}
QTreeView[sortingEnabled=false] QHeaderView::down-arrow,
QTreeView[sortingEnabled=false] QHeaderView::up-arrow,
QTableView[sortingEnabled=false] QHeaderView::down-arrow,
QTableView[sortingEnabled=false] QHeaderView::up-arrow {
    width: 0;
    padding: 0;
}
QCalendarWidget {
    border: none;
}
QCalendarWidget > .QWidget {
    background: #ffffff;
    border-bottom: 1px solid #dadce0;
    border-radius: 4px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
}
QCalendarWidget > .QWidget > QWidget {
    padding: 1px;
}
QCalendarWidget > .QWidget > QSpinBox {
    margin-left: 1px;
}
QCalendarWidget > .QWidget > QSpinBox::up-button,
QCalendarWidget > .QWidget > QSpinBox::down-button {
    margin: 1px 3px 1px 1px;
}
QCalendarWidget > QTableView {
    margin: 0;
    border: none;
    border-radius: 4px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
QCalendarWidget > .QWidget > QToolButton#qt_calendar_prevmonth {
    qproperty-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
}
QCalendarWidget > .QWidget > QToolButton#qt_calendar_nextmonth {
    qproperty-icon: url(${path}/themes/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
}
QLineEdit,
QAbstractSpinBox {
    border: 1px solid #dadce0;
    padding: 3px 4px;
    min-height: 1em;
    background: #f8f9fa;
    border-radius: 4px;
}
QLineEdit:focus,
QAbstractSpinBox:focus {
    border: 1px solid #0081db;
}
QAbstractSpinBox::up-button,
QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    width: 12px;
    height: 4px;
    padding: 3px;
    border-radius: 0;
}
QAbstractSpinBox::up-button:hover,
QAbstractSpinBox::down-button:hover {
    background: #e2eafb;
}
QAbstractSpinBox::up-button {
    subcontrol-position: top right;
    margin: 3px 3px 1px 1px;
}
QAbstractSpinBox::up-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/themes/light/svg/arrow_drop_up__icon-foreground.svg);
}
QAbstractSpinBox::up-arrow:disabled {
    image: url(${path}/themes/light/svg/arrow_drop_up__icon-foreground-disabled.svg);
}
QAbstractSpinBox::down-button {
    subcontrol-position: bottom right;
    margin: 1px 3px 3px 1px;
}
QAbstractSpinBox::down-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/themes/light/svg/arrow_drop_up__icon-foreground__rotate-180.svg);
}
QAbstractSpinBox::down-arrow:disabled {
    image: url(${path}/themes/light/svg/arrow_drop_up__icon-foreground-disabled__rotate-180.svg);
}
QDateTimeEdit::drop-down {
    subcontrol-position: center right;
    padding-right: 4px;
    width: 16px;
    image: url(${path}/themes/light/svg/calendar_today__icon-foreground.svg);
}
QDateTimeEdit::drop-down:disabled {
    image: url(${path}/themes/light/svg/calendar_today__icon-foreground-disabled.svg);
}
QDateTimeEdit::down-arrow[calendarPopup=true] {
    image: none;
}
QDateTimeEdit QAbstractItemView {
    border: 1px solid #0081db;
}
QDateTimeEdit QCalendarWidget QAbstractItemView {
    padding: -1px;
    border: none;
}
QFileDialog > QFrame QAbstractItemView {
    border: none;
}
QFileDialog > QFrame > QFrame QFrame QFrame {
    border: none;
    padding: 0;
}
QFontDialog QListView {
    min-height: 60px;
}
QFontDialog QScrollBar:vertical {
    margin: 0;
}
QComboBox::indicator:checked,
QMenu::indicator:checked {
    width: 18px;
    image: url(${path}/themes/light/svg/check__icon-foreground.svg);
}
QMenu::indicator {
    width: 18px;
    background: #c4c7cc;
    border-radius: 4px;
    margin-left: 3px;
}
QCheckBox,
QRadioButton {
    spacing: 8px;
}
QGroupBox::title {
    spacing: 6px;
}
QCheckBox::indicator,
QGroupBox::indicator,
QAbstractItemView::indicator,
QRadioButton::indicator {
    height: 14px;
    width: 14px;
    border-radius: 2px;
}
QCheckBox::indicator,
QGroupBox::indicator,
QAbstractItemView::indicator {
    border-image: url(${path}/themes/light/svg/check_box_outline_blank__icon-foreground.svg)
}
QRadioButton::indicator {
    border-image: url(${path}/themes/light/svg/radio_button_unchecked__icon-foreground.svg)
}
QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled,
QAbstractItemView::indicator:unchecked:disabled {
    border-image: url(${path}/themes/light/svg/check_box_outline_blank__icon-foreground-disabled.svg)
}
QCheckBox::indicator:checked,
QGroupBox::indicator:checked,
QAbstractItemView::indicator:checked {
    background: #0081db;
    border-image: unset;
    image: url(${path}/themes/light/svg/check__base.svg);
}
QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled,
QAbstractItemView::indicator:checked:disabled {
    background: #babdc2;
    image: url(${path}/themes/light/svg/check__base.svg);
}
QCheckBox::indicator:indeterminate,
QAbstractItemView::indicator:indeterminate {
    background: #0081db;
    border-image: unset;
    image: url(${path}/themes/light/svg/horizontal_rule__base.svg);
}
QCheckBox::indicator:indeterminate:disabled,
QAbstractItemView::indicator:indeterminate:disabled {
    background: #babdc2;
    border-color: #babdc2;
    image: url(${path}/themes/light/svg/horizontal_rule__base.svg);
}
QRadioButton::indicator:checked {
    height: 12px;
    width: 12px;
    background: #0081db;
    border: 1px solid #0081db;
    border-radius: 7px;
    border-image: unset;
    image: url(${path}/themes/light/svg/trip_origin__base.svg);
}
QRadioButton::indicator:checked:disabled {
    background: #babdc2;
    border: 1px solid #babdc2;
}
QRadioButton::indicator:unchecked:disabled {
    border-image: url(${path}/themes/light/svg/radio_button_unchecked__icon-foreground-disabled.svg)
}
QMenu {
    $env_patch{"version": "<6.0.0", "value": "border-radius: 8px"};
}
QComboBox QAbstractItemView {
    $env_patch{"version": ">=6.0.0", "value": "border-radius: 0; margin: 0"};
}
QStatusBar > QMenu {
    $env_patch{"version": ">=6.0.0", "value": "border-radius: 0; margin: 0"};
}
PlotWidget {
    padding: 0;
}

"""
