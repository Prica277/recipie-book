""" 
Filename: home_screen.py
Author: Alex Price
Description: The layout for the home screen of the Recipe Index app.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QBoxLayout,
    QGridLayout,
    QStackedLayout,
    QWidget,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
)
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Recipe Index - Home")

        pagelayout = QBoxLayout
        button_layout = QGridLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        widget = QLabel("Recipe Index")
        font = widget.font()
        font.setPointSize(30)
        #widget.setFont(Josefin Sans)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.stacklayout.addWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
