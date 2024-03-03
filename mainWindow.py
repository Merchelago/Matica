from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matica")
        button_save = QAction('Save', self)
        button_load = QAction("Load", self)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_save)
        file_menu.addAction(button_load)
