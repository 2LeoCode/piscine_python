from functools import partial

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "argula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe_names():
    print(
        "\nList of recipes:\n  "
        f"{f'{chr(10)}  '.join([name for name in cookbook.keys()])}"
    )


def print_recipe_details():
    name = input("\nPlease enter a recipe name to get its details:\n")
    try:
        print(
            f"\nRecipe for {name}:\n"
            f"  Ingredients list: {', '.join(cookbook[name]['ingredients'])}\n"
            f"  To be eaten for {cookbook[name]['meal']}.\n"
            f"  Takes {cookbook[name]['prep_time']} minutes of cooking."
        )
    except KeyError:
        print("\nRecipe not found")


def remove_recipe():
    name = input("\n>>> Enter a name:\n")
    try:
        del cookbook[name]
    except KeyError:
        print("\nRecipe not found")
    else:
        print(f"\nRecipe {name} deleted from the cookbook.")


def add_recipe():
    name = input("\n>>> Enter a name:\n")
    print("\n>>> Enter ingredients:")
    ingredients = []
    while True:
        current_ingredient = input()
        if current_ingredient == "":
            break
        ingredients.append(current_ingredient)
    while True:
        meal = input(">>> Enter a meal:\n")
        if meal in ["breakfast", "lunch", "dinner", "dessert"]:
            break
        print(
            "Meal must be one of the following: "
            "breakfast, lunch, dinner, dessert\n"
        )
    while True:
        try:
            prep_time = int(input("\n>>> Enter a preparation time:\n"))
        except ValueError:
            print("Preparation time must be an integer")
        else:
            break
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"\nRecipe {name} added to the cookbook !")


def close_cookbook():
    print("\nCookbook closed. Goodbye !")
    exit()


if __name__ == "__main__":
    print_options = partial(
        print,
        "List of available options:\n"
        "  1: Add a recipe\n"
        "  2: Delete a recipe\n"
        "  3: Print a recipe\n"
        "  4: Print the cookbook\n"
        "  5: Quit"
    )
    print("Welcome to the Python Cookbook!")
    print_options()
    while True:
        while True:
            try:
                choice = int(input("\nPlease select an option:\n>> "))
            except ValueError:
                print("Choice must be an integer")
            else:
                break
        try:
            {
                1: add_recipe,
                2: remove_recipe,
                3: print_recipe_details,
                4: print_recipe_names,
                5: close_cookbook
            }[choice]()
        except KeyError:
            print("Sorry, this option does not exist")
