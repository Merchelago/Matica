from PySide6.QtCore import QSize, Qt, QPoint
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QScrollArea,
    QWidget,
    QVBoxLayout,
    QPushButton,
)

from infiniteWorkspace import InfiniteWorkspace


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matica")
        button_save = QAction('Save', self)
        button_save_as = QAction('Save as', self)
        button_load = QAction("Load", self)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_save)
        file_menu.addAction(button_save_as)
        file_menu.addAction(button_load)

        self.work = InfiniteWorkspace()
        self.setCentralWidget(self.work)

        self.setFixedSize(800, 600)