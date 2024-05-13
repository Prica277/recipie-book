""" 
Filename: app.py
Author: Alex Price
Description: The main controller for the app layouts.
"""
import sys
from PyQt6.QtGui import QPalette, QColor, QFontDatabase, QFont
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QGridLayout,
    QVBoxLayout,
    QStackedLayout,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        #setting minor window details
        self.setWindowTitle("Recipe Index")
        self.setFixedSize(517, 442)

        #create layouts
        #self.layout = QVBoxLayout()
        home_layout = QGridLayout()
        calculator_layout = QGridLayout()
        selector_layout = QGridLayout()
        show_layout = QGridLayout()
        self.stacked_layout = QStackedLayout()
        
        # self.layout.addLayout(main_layout)
        #self.stacked_layout.addStretch()

        #creating first screen
        self.main_screen = QWidget()
        self.main_screen.setLayout(home_layout)
        self.stacked_layout.addWidget(self.main_screen)

        #title label
        title_label = QLabel("Recipe Index - Home")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        #align & size the title label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        #coloring title label
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        #add title label
        home_layout.addWidget(title_label, 0, 0, 1, 4)

        #welcome label
        welcome_label = QLabel("Welcome to Recipe Index! A digital cookbook built by you, just for you!")
        welcome_label.setFont(QFont("Josefin Sans", 10))
        welcome_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        home_layout.addWidget(welcome_label, 1, 0, 1, 4)

        #view label
        view_label = QLabel("View Recipe")
        view_label.setFont(QFont("Josefin Sans", 15))
        view_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        home_layout.addWidget(view_label, 2, 0, 1, 2)

        #view button
        view_button = QPushButton("Go!")
        view_button.setFont(QFont("Josefin Sans", 15))
        view_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        view_button.clicked.connect(self.double_page)
        home_layout.addWidget(view_button, 2, 2, 1, 2)

        #edit label
        edit_label = QLabel("Edit Recipe")
        edit_label.setFont(QFont("Josefin Sans", 15))
        edit_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        edit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        home_layout.addWidget(edit_label, 3, 0, 1, 2)

        #edit button
        edit_button = QPushButton("Go!")
        edit_button.setFont(QFont("Josefin Sans", 15))
        edit_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        #edit_button.clicked.connect(self.next_page)
        home_layout.addWidget(edit_button, 3, 2, 1, 2)

        #conversions label
        conversions_label = QLabel("Conversions")
        conversions_label.setFont(QFont("Josefin Sans", 15))
        conversions_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        conversions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        home_layout.addWidget(conversions_label, 4, 0, 1, 2)

        #conversions button
        conversions_button = QPushButton("Go!")
        conversions_button.setFont(QFont("Josefin Sans", 15))
        conversions_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        conversions_button.clicked.connect(self.next_page)
        home_layout.addWidget(conversions_button, 4, 2, 1, 2)

        #calculator screen
        self.calculator_screen = QWidget()
        self.calculator_screen.setLayout(calculator_layout)
        self.stacked_layout.addWidget(self.calculator_screen)

        #title label
        title_label = QLabel("Recipe Index - Conversions")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        calculator_layout.addWidget(title_label, 0, 0, 1, 4)

        #selection combo box
        measurement_selector = QComboBox()
        measurement_selector.setFont(QFont("Josefin Sans", 10))
        measurement_selector.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        measurement_selector.addItems(["inital measure", "tsp", "tbsp", "1/4 cups", "1/3 cups", "1/2 cups", "1 cup"])
        calculator_layout.addWidget(measurement_selector, 1, 0, 1, 2)

        #converting measure
        convert_measurement_selector = QComboBox()
        convert_measurement_selector.setFont(QFont("Josefin Sans", 10))
        convert_measurement_selector.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        convert_measurement_selector.addItems(["conversion measure","tsp", "tbsp", "1/4 cups", "1/3 cups", "1/2 cups", "1 cup"])
        calculator_layout.addWidget(convert_measurement_selector, 1, 2, 1, 2)

        #output label
        measurement_output_label = QLabel()
        measurement_output_label.setFont(QFont("Josefin Sans", 10))
        measurement_output_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        calculator_layout.addWidget(measurement_output_label, 3, 0, 1, 4)

        #back button
        return_button = QPushButton("Return")
        return_button.setFont(QFont("Josefin Sans", 15))
        return_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        return_button.clicked.connect(self.previous_page)
        calculator_layout.addWidget(return_button, 4, 1, 1, 2)

        #recipe selector screen
        self.recipe_selector_screen = QWidget()
        self.recipe_selector_screen.setLayout(selector_layout)
        self.stacked_layout.addWidget(self.recipe_selector_screen)

        #title label
        title_label = QLabel("Recipe Index - Selector")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        selector_layout.addWidget(title_label, 0, 0, 1, 4)

        #return
        return_button = QPushButton("Return")
        return_button.setFont(QFont("Josefin Sans", 15))
        return_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        return_button.clicked.connect(self.home_page)
        selector_layout.addWidget(return_button, 4, 1, 1, 3)

        #go to recipe output screen
        output_button = QPushButton("Go!")
        output_button.setFont(QFont("Josefin Sans", 15))
        output_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        output_button.clicked.connect(self.next_page)
        selector_layout.addWidget(output_button, 4, 2, 1, 2)
        
        #recipe output screen
        self.view_recipe_screen = QWidget()
        self.view_recipe_screen.setLayout(show_layout)
        self.stacked_layout.addWidget(self.view_recipe_screen)

        #title label
        title_label = QLabel("Recipe Index - View")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        show_layout.addWidget(title_label, 0, 0, 1, 4)  

        self.setLayout(self.stacked_layout)
        

    def next_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 1)
    
    def double_page(self):
        for i in range (2):
            self.stacked_layout.setCurrentIndex(
                self.stacked_layout.currentIndex() + 1)
    
    def triple_page(self):
        for i in range (3):
            self.stacked_layout.setCurrentIndex(
                self.stacked_layout.currentIndex() + 1)
        
    def previous_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 1)
        
    def home_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 2
        )
    
    def return_home_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 3
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()

