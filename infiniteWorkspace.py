from PySide6.QtCore import QSize, Qt, QPoint, QRect
from PySide6.QtGui import QAction, QIcon, QPainter, QColor, QPixmap
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
    QPushButton, QGridLayout, QSizePolicy,
)



class InfiniteWorkspace(QWidget):
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)  # Включаем отслеживание движения мыши

        self.scale_factor = 1.0  # Масштабирование

        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        # Создаем и добавляем прозрачные ячейки для демонстрации бесконечной области
        for i in range(10):
            transparent_button = QPushButton(f"{i}")
            self.layout.addWidget(transparent_button)

        # Устанавливаем компоновку основного окна
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.widget)
        self.setLayout(main_layout)

        self.drag_start_pos = QPoint()  # Переменная для хранения начальной позиции перетаскивания

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # Рассчитываем разницу между текущей и начальной позицией
            drag_distance = event.pos() - self.drag_start_pos
            # Смещаем рабочую область на расстояние, на которое переместилась мышь
            self.widget.move(self.widget.pos() + drag_distance)
            # Сохраняем текущую позицию как начальную для следующего события перемещения
            self.drag_start_pos = event.pos()

    def wheelEvent(self, event):
        # Устанавливаем масштабирование с помощью колеса мыши
        if event.angleDelta().y() > 0:
            self.scale_factor *= 1.1
        else:
            self.scale_factor *= 0.9

        self.updateGeometry()

    def updateGeometry(self):
        # Обновляем масштаб прозрачных ячеек
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i).widget()
            item.setFixedSize(QSize(50 * self.scale_factor, 50 * self.scale_factor))

    def paintEvent(self, event):
        # Рисуем клетчатый фон
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(240, 0, 0))  # Цвет клеток
        cell_size = 50
        scaled_cell_size = cell_size * self.scale_factor
        for x in range(0, int(self.width() / scaled_cell_size) + 1):
            for y in range(0, int(self.height() / scaled_cell_size) + 1):
                rect = QRect(x * scaled_cell_size, y * scaled_cell_size, scaled_cell_size, scaled_cell_size)
                painter.drawRect(rect)