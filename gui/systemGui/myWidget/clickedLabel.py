from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal,Qt


class clickedLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()