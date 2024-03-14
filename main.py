from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    with open('styles.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
