class Recipe:
    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients: list,
        recipe_type: str,
        description: str = None,
    ):
        assert (
            isinstance(name, str) and name
        ), "name must be a non-empty string"
        assert isinstance(cooking_lvl, int), "cooking_lvl must be an integer"
        assert 1 <= cooking_lvl <= 5, "cooking_lvl must be between 1 and 5"
        assert isinstance(cooking_time, int), "cooking_time must be an integer"
        assert cooking_time >= 0, "cooking_time must be positive"
        assert (
            isinstance(ingredients, list) and ingredients
        ), "ingredients must be a non-empty list"
        assert (
            isinstance(recipe_type, str) and recipe_type
        ), "recipe_type must be a non-empty string"
        assert (
            recipe_type in ["starter", "lunch", "dessert"]
        ), "recipe_type must be one of starter, lunch, dessert"
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return (
            f"Recipe for {self.name}:\n"
            f"  Cooking level: {self.cooking_lvl}\n"
            f"  Cooking time: {self.cooking_time}\n"
            f"  Ingredients:\n    {f'{chr(10)}    '.join(self.ingredients)}\n"
            f"  Description: {self.description}\n"
            f"  Recipe type: {self.recipe_type}"
        )
