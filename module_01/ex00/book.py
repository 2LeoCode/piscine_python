from datetime import datetime
from itertools import chain
from recipe import Recipe


class Book:
    def __init__(self, name: str):
        assert (
            isinstance(name, str) and name
        ), "name must be a non-empty string"
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list: 'dict[str, list[Recipe]]' = {
            "starter": [],
            "lunch": [],
            "dessert": [],
        }

    def get_recipe_by_name(self, name: str):
        found = [
            recipe for recipe in list(
                chain.from_iterable(self.recipes_list.values())
            ) if recipe.name == name
        ]
        if len(found):
            print(str(found[0]))
            return found[0]
        raise AssertionError("Recipe not found")

    def get_recipes_by_types(self, recipe_type: str):
        if recipe_type not in self.recipes_list:
            raise AssertionError("Recipe type doesn't exist")
        print(f"Recipes for {recipe_type}:")
        output = "\n\n".join([
            f"  {str(recipe).replace(f'{chr(10)}', f'{chr(10)}  ')}"
            for recipe in self.recipes_list[recipe_type]
        ])
        print(output)
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: Recipe):
        assert isinstance(recipe, Recipe), "recipe must be a Recipe instance"
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
