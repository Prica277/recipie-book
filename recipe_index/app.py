""" 
Filename: app.py
Author: Alex Price
Description: The main controller for the app layouts.
"""
import sys
from PyQt6.QtGui import QPalette, QColor, QFontDatabase, QFont, QIcon
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QGridLayout,
    QStackedLayout,
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
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
        salmon_layout = QGridLayout()
        quiche_layout = QGridLayout()
        skillet_layout = QGridLayout()
        paella_layout = QGridLayout()
        lemon_layout = QGridLayout()
        seven_layout = QGridLayout()
        choco_layout = QGridLayout()
        cowboy_layout = QGridLayout()
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

        # recipe_selector = QComboBox()
        # recipe_selector.setFont(QFont("Josefin Sans", 10))
        # recipe_selector.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        # recipe_selector.addItems(["Salmon", "Quiche", "Skillet Meal", "Shrimp Paella", "Lemon Bars", "Seven-Layer Bars", "Cowboy Cookies", "Chocolate-Chip Cookies", "Peanut-butter Cookies"])
        # selector_layout.addWidget(recipe_selector, 1, 0, 1, 4)

        #recipe buttons
        salmon = QPushButton("Salmon")
        salmon.setFont(QFont("Josefin Sans", 12))
        salmon.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        salmon.clicked.connect(self.next_page)
        selector_layout.addWidget(salmon, 1, 0, 1, 1)

        quiche = QPushButton("Quiche")
        quiche.setFont(QFont("Josefin Sans", 12))
        quiche.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        quiche.clicked.connect(self.quiche_page)
        selector_layout.addWidget(quiche, 1, 1, 1, 1)

        skillet = QPushButton("Skillet Meal")
        skillet.setFont(QFont("Josefin Sans", 12))
        skillet.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        skillet.clicked.connect(self.skillet_page)
        selector_layout.addWidget(skillet, 1, 2, 1, 1)

        paella = QPushButton("Shrimp Paella")
        paella.setFont(QFont("Josefin Sans", 12))
        paella.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        paella.clicked.connect(self.paella_page)
        selector_layout.addWidget(paella, 1, 3, 1, 1)

        l_bars = QPushButton("Lemon Bars")
        l_bars.setFont(QFont("Josefin Sans", 12))
        l_bars.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        l_bars.clicked.connect(self.lemon_page)
        selector_layout.addWidget(l_bars, 2, 0, 1, 1)

        seven_bars = QPushButton("7 Layer Bars")
        seven_bars.setFont(QFont("Josefin Sans", 12))
        seven_bars.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        seven_bars.clicked.connect(self.seven_page)
        selector_layout.addWidget(seven_bars, 2, 1, 1, 1)

        choco_cookie = QPushButton("ChocChip Cookie")
        choco_cookie.setFont(QFont("Josefin Sans", 12))
        choco_cookie.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        choco_cookie.clicked.connect(self.choco_page)
        selector_layout.addWidget(choco_cookie, 2, 2, 1, 1)

        cowboy_cookie = QPushButton("Cowboy Cookie")
        cowboy_cookie.setFont(QFont("Josefin Sans", 12))
        cowboy_cookie.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:95px;")
        cowboy_cookie.clicked.connect(self.cowboy_page)
        selector_layout.addWidget(cowboy_cookie, 2, 3, 1, 1)

        #return
        return_button = QPushButton("Back")
        return_button.setFont(QFont("Josefin Sans", 15))
        return_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        return_button.clicked.connect(self.home_page)
        selector_layout.addWidget(return_button, 4, 1, 1, 2)
        
        #recipe output screens
        self.view_salmon = QWidget()
        self.view_salmon.setLayout(salmon_layout)
        self.stacked_layout.addWidget(self.view_salmon)

        #title label
        title_label = QLabel("Recipe Index - View")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        salmon_layout.addWidget(title_label, 0, 0, 1, 4)

        #dish type
        dish_label = QLabel("Dish Type: Entreé")
        dish_label.setFont(QFont("Josefin Sans", 10))
        dish_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        salmon_layout.addWidget(dish_label, 1, 0, 1, 1)

        #prep time
        prep = QLabel("Prep Time: 15 min")
        prep.setFont(QFont("Josefin Sans", 10))
        prep.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        salmon_layout.addWidget(prep, 1, 1, 1, 1)

        #total time
        total = QLabel("Total Time: 30 min")
        total.setFont(QFont("Josefin Sans", 10))
        total.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        salmon_layout.addWidget(total, 1, 2, 1, 1)

        #servings 
        servings = QLabel("Servings: 6")
        servings.setFont(QFont("Josefin Sans", 10))
        servings.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        salmon_layout.addWidget(servings, 1, 3, 1, 1)

        #steps list
        steps = QListWidget()
        steps.addItems(["Ingredients: ", "- 2 pound side of salmon", "- 2 tablespoons olive oil", "- 2 small lemons", "- Additional fresh herbs", 
                        " ", "Instructions: ", "- Remove salmon from the refridgerator and let stand at room temperature for 10", 
                        "    minutes while you prepare the other ingredients. Heat oven to 375 degrees F.",
                        "    Line a large baking dish with a large piece of aluminum foil",
                        "- Lightly coat the foil with baking spray, then cut one lemon into thin slices",
                        "    and arrange half the slices and fresh herbs down the center.",
                        "    Place the salmon on top.",
                        "- Drizzle the salmon with oil and lay the remaining lemon slices and herbs on top.",
                        "    Juice the other lemon and pour the juice on top as well.",
                        "- Fold the sides of the foil up and over top of the salmon until it is completely",
                        "    enclosed and forms a sealed packet. Leave a little room for air to circulate.",
                        "- Bake the salmon for 15 - 20 minutes, until the salmon is almost completely ",
                        "    cooked through at the thickest part. The cooking time will vary based on the",
                        "    thickness of the salmon. If your side is around 1 inch thick, check earlier.",
                        "    If your side is around 1 1/2 inches or more thick, it may need longer.",
                        "- Remove salmon from oven and carefully open foil so the top of the fish is ",
                        "    completely uncovered. Change the oven settings to broil and broil the fish ",
                        "    for three minutes until the top is slightly golden and it is cooked through.",
                        "    Watch closely to ensure it doesn't burn. Remove from oven, as salmon can",
                        "    progress from underdone to overdone very quickly.",
                        "- To serve, cut salmon into portions and top with fresh herbs or lemon as desired.",
                        "    If you wish for the author to murder you, add ketchup."
                        ])
        steps.setFont(QFont("Josefin Sans", 10))
        steps.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        salmon_layout.addWidget(steps, 2, 0, 2, 4)

        #reset button
        reset_button = QPushButton("Back")
        reset_button.setFont(QFont("Josefin Sans", 15))
        reset_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        reset_button.clicked.connect(self.return_home_page)
        salmon_layout.addWidget(reset_button, 4, 1, 1, 2)

        #quiche
        self.view_quiche = QWidget()
        self.view_quiche.setLayout(quiche_layout)
        self.stacked_layout.addWidget(self.view_quiche)

        #title label
        title_label = QLabel("Recipe Index - View")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        quiche_layout.addWidget(title_label, 0, 0, 1, 4)

        #dish type
        dish_label = QLabel("Dish Type: Pie")
        dish_label.setFont(QFont("Josefin Sans", 10))
        dish_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        quiche_layout.addWidget(dish_label, 1, 0, 1, 1)

        #prep time
        prep = QLabel("Prep Time: 15 min")
        prep.setFont(QFont("Josefin Sans", 10))
        prep.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        quiche_layout.addWidget(prep, 1, 1, 1, 1)

        #total time
        total = QLabel("Total Time: 65 min")
        total.setFont(QFont("Josefin Sans", 10))
        total.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        quiche_layout.addWidget(total, 1, 2, 1, 1)

        #servings 
        servings = QLabel("Servings: 8")
        servings.setFont(QFont("Josefin Sans", 10))
        servings.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        quiche_layout.addWidget(servings, 1, 3, 1, 1)

        #steps list
        steps = QListWidget()
        steps.addItems(["Ingredients: ", "- 1 9-inch pie crust", "- 1 egg yolk, beaten", "- 3 eggs", "- 1 cup shredded chedder cheese",
                        "- 1 cup chopped cooked ham", "- 1 cup broccoli florets", "- 1 cup skim milk", "- 3/4 tsp salt", "- 1/4 tsp pepper",
                        " ", "Instructions: ", 
                        "- Preheat oven to 375 degrees F, and prepare pie crust according to package.",
                        "- Brush pie crust with the egg yolk. Sprinkle shredded cheese, ham, and",
                        "    broccoli. Place the pie shell onto a baking sheet lined with aluminum foil.",
                        "- In a medium bowl, whisk the eggs and milk together. Add the salt and pepper, ",
                        "    and stir to combine. Pour the mixture into the pie shell until around 3/4",
                        "    full.",
                        "- Place the baking tray in the oven and bake for 40-45 minutes, until set.",
                        "- Let the quiche cool for 10 minutes before slicing, so it sets up.",
                        "- Serve warm and enjoy!"
                        ])
        steps.setFont(QFont("Josefin Sans", 10))
        steps.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        quiche_layout.addWidget(steps, 2, 0, 2, 4)

        #reset button
        reset_button = QPushButton("Back")
        reset_button.setFont(QFont("Josefin Sans", 15))
        reset_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        reset_button.clicked.connect(self.back_quiche)
        quiche_layout.addWidget(reset_button, 4, 1, 1, 2)

        #skillet
        self.view_skillet = QWidget()
        self.view_skillet.setLayout(skillet_layout)
        self.stacked_layout.addWidget(self.view_skillet)

        #title label
        title_label = QLabel("Recipe Index - View")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        skillet_layout.addWidget(title_label, 0, 0, 1, 4)

        #dish type
        dish_label = QLabel("Dish Type: Entrée")
        dish_label.setFont(QFont("Josefin Sans", 10))
        dish_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        skillet_layout.addWidget(dish_label, 1, 0, 1, 1)

        #prep time
        prep = QLabel("Prep Time: 5 min")
        prep.setFont(QFont("Josefin Sans", 10))
        prep.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        skillet_layout.addWidget(prep, 1, 1, 1, 1)

        #total time
        total = QLabel("Total Time: 30 min")
        total.setFont(QFont("Josefin Sans", 10))
        total.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        skillet_layout.addWidget(total, 1, 2, 1, 1)

        #servings 
        servings = QLabel("Servings: 6")
        servings.setFont(QFont("Josefin Sans", 10))
        servings.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        skillet_layout.addWidget(servings, 1, 3, 1, 1)

        #steps list
        steps = QListWidget()
        steps.addItems(["Ingredients: ", "- 3 tbsp oil", "- 1/2 medium onion, diced finely", "- 1 lb diced chicken breast",
                        "- 2 cloves garlic, minced", "- 1 C uncooked long-grain white rice", "- 2 1/2 C chicken broth", 
                        "- 2 1/2 C broccoli florets", "- 2 C shredded chedder cheese", " ", "Instructions: ", 
                        ])
        steps.setFont(QFont("Josefin Sans", 10))
        steps.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        skillet_layout.addWidget(steps, 2, 0, 2, 4)

        #reset button
        reset_button = QPushButton("Back")
        reset_button.setFont(QFont("Josefin Sans", 15))
        reset_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        reset_button.clicked.connect(self.back_skillet)
        skillet_layout.addWidget(reset_button, 4, 1, 1, 2)

        #paella
        self.view_paella = QWidget()
        self.view_paella.setLayout(paella_layout)
        self.stacked_layout.addWidget(self.view_paella)

        #title label
        title_label = QLabel("Recipe Index - View")
        title_label.setFont(QFont("Josefin Sans", 20, 800))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("background-color:#AD8B73; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        paella_layout.addWidget(title_label, 0, 0, 1, 4)

        #dish type
        dish_label = QLabel("Dish Type: Entrée")
        dish_label.setFont(QFont("Josefin Sans", 10))
        dish_label.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        paella_layout.addWidget(dish_label, 1, 0, 1, 1)

        #prep time
        prep = QLabel("Prep Time: 10 min")
        prep.setFont(QFont("Josefin Sans", 10))
        prep.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        paella_layout.addWidget(prep, 1, 1, 1, 1)

        #total time
        total = QLabel("Total Time: 45 min")
        total.setFont(QFont("Josefin Sans", 10))
        total.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        paella_layout.addWidget(total, 1, 2, 1, 1)

        #servings 
        servings = QLabel("Servings: 4")
        servings.setFont(QFont("Josefin Sans", 10))
        servings.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        paella_layout.addWidget(servings, 1, 3, 1, 1)

        #steps list
        steps = QListWidget()
        steps.addItems(["Ingredients: ", "- 1 lb jumbo shrimp, frozen with shell on", "- 1 C jasmine rice", "- 4 TBSP butter",
                        "- 1 onion, diced", "- 4 cloves minced garlic", "- 1 C chicken broth", "- 1/2 C white wine",
                        " ", "Instructions: ", "- Set Instant Pot to saute function, and melt butter in it.",
                        "    Add onion and cook until softened. Add garlic and cook a minute more.",
                        "- Add chicken broth, white wine, and rice. Stir and cook for a minute. Deglaze ",
                        "    your pot by stirring to ensure nothing is sticking to the bottom.",
                        "- Add shrimp to pot. Turn off Instant Pot and cover. Ensure valve is in sealing.",
                        "- Set Instant Pot to pressure cook for five minutes. When done, quick release.",
                        "- Remove from Instant Pot and serve.",
                        ])
        steps.setFont(QFont("Josefin Sans", 10))
        steps.setStyleSheet("background-color:#E3CAA5; color:#3E3028; border-radius:4px; padding:10px; height:50px;")
        paella_layout.addWidget(steps, 2, 0, 2, 4)

        #reset button
        reset_button = QPushButton("Back")
        reset_button.setFont(QFont("Josefin Sans", 15))
        reset_button.setStyleSheet("background-color:#CEAB93; color:#3E3028; border-radius:4px; padding:10px; height:30px;")
        reset_button.clicked.connect(self.back_paella)
        paella_layout.addWidget(reset_button, 4, 1, 1, 2)


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

    def salmon_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 1
        )
    
    def quiche_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 2
        )

    def back_quiche(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 4
        )

    def skillet_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 3
        )
    
    def back_skillet(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 5
        )
    
    def paella_page (self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 4
        )
    
    def back_paella(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 6
        )

    def lemon_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 5
        )

    def seven_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 6
        )

    def choco_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 7
        )

    def cowboy_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 8
        )

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()

