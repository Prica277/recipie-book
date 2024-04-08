""" 
Filename: utilities.py
Author: Alex Price
Description: A set of functions to be used to make the program more useful and 
be used in similar projects.
"""

# import statements
from pathlib import Path
import json

def get_file_contents(path: str, filename: str):
    """Returns the contents of the file in the path.
    
    Args:
        path: the relative folder path should end with a forward slash (/)
        filename: the name of the file with extension

    Returns:
        contents: a string of the file contents"""
    
    folder = Path(path)
    file_to_open = folder / filename
    f = open(file_to_open)
    return f.read()


def get_menu_choice(menu: str, legal_choices: tuple) -> str:
    """displays a menu of options, and asks the user to make a choice.
    
    Args:
        menu: a formatted string of choices for the user
        legal_choices: a tuple of only choices the user is allowed to 
            make

    Returns:
        user_choices: a single character that must be one of the legal choices
    """

    user_choice = ""
    while user_choice not in legal_choices:
        print(menu)
        user_choice = input("Your Choice: ")
        # Give feedback if user didn't use proper choice
        if user_choice not in legal_choices:
            print("Sorry, that is not an option. Please select one of the following: ")
            print(legal_choices)

    return user_choice