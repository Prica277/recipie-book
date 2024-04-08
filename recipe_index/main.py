""" 
Filename: main.py
Author: Alex Price
Description: The bulk of the project's code.
"""
import utilities

def main():
    # Create a menu of choices upon starting the program
    new_menu = """
    Here is your list of options:

        1 - Option 1: Pick a recipe
        2 - Option 2: Change measurements of a recipe
        3 - Option 3: Save a new recipe
        4 - Option 4: Quit
    """
    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        if choice == "1":
            # opens up the main database to search from.
            pick_recipe()
            # print("\nWe're working hard to bring this function up and running! Why not try another function?")
        elif choice == "2":
            # opens a new file that allows the user to pick the recipe and then 
            # change the amount desired. It would then adjust the ingredient amounts accordingly.
            print("\nSorry, this function is still under construction! Why not try another function?")
        elif choice == "3":
            # edits the main cookie dictionary to add the newest recipe.
            print("\nWe're still hammering out the bugs in this function. Why not try another function?")
    if choice == "4":
        print("\nGoodbye!")

def pick_recipe():
    """opens up the main cookie dictionary to search from."""
    
    print("\nHere's all the recipies you currently have to pick from: ")
    #UNDER CONSTRUCTION
    
    # gets the user's input and converts it into the correct format to be searched for.
    desired_recipe = input("Enter the recipe you're looking for! Be sure to spell it correctly: ")
    desired_recipe = desired_recipe.lower()
    user_recipe = ""
    for i in range(len(desired_recipe)):
        if desired_recipe[i] == " ":
            user_recipe = user_recipe + "_"
        else:
            user_recipe = user_recipe + desired_recipe[i]
    print("You chose " + desired_recipe + ". Is this right?")
    cont = input("Y/N: ")
    cont = cont.upper()
    if cont == "N":
        #loops through the entire process again and returns to this check.
        pick_recipe()
    elif cont == "Y": 
        print("Hooray!")
        #continues to the next step.
        #display_recipe(user_recipe, recipes)
    else:
        print("Sorry, you've encountered an error. Please try again.")
        pick_recipe()