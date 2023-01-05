from book import Book
from recipe import Recipe
from sys import stderr

# Create a book
book = Book("foo")

# Create a recipe
recipe = Recipe(
    name="foo",
    cooking_lvl=1,
    cooking_time=10,
    ingredients=["foo", "bar"],
    recipe_type="starter",
    description="foo bar baz"
)

# Create another recipe
recipe2 = Recipe(
    name="bar",
    cooking_lvl=2,
    cooking_time=20,
    ingredients=["bar", "baz"],
    recipe_type="starter"
)

# Create another recipe in lunch
recipe3 = Recipe(
    name="baz",
    cooking_lvl=3,
    cooking_time=30,
    ingredients=["baz", "qux"],
    recipe_type="lunch",
    description="baz qux quux"
)

# Add the recipe to the book
book.add_recipe(recipe)

# Add the other recipe to the book
book.add_recipe(recipe2)

# Add the third recipe to the book
book.add_recipe(recipe3)

# Get a recipe by name
foo = book.get_recipe_by_name("baz")
print()

# Then print it from the result
print(f"{foo}\n")

# Get the recipe by type
starters = book.get_recipes_by_types("starter")

# Print the result
result = (
    f"{chr(10)}  ".join([
        str(recipe).replace(f'{chr(10)}', f'{chr(10)}  ')
        for recipe in starters
    ])
)
print(f"\nRecipes for starter:\n  {result}\n")

print()

# Error cases for Recipe

# Error cases for name
try:
    err_recipe = Recipe(
        name=1,
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_recipe = Recipe(
        name="",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for cooking_lvl

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl="1",
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=0,
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for cooking_time

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time="10",
        ingredients=["foo", "bar"],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time=-10,
        ingredients=["foo", "bar"],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for ingredients

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time=10,
        ingredients="foo",
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=[],
        recipe_type="starter",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for recipe_type

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type=1,
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type="",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_recipe = Recipe(
        name="foo",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["foo", "bar"],
        recipe_type="foo",
        description="foo bar baz"
    )
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for Book

# Error cases for name

try:
    err_book = Book("")
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    err_book = Book(1)
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for add_recipe

try:
    book.add_recipe("foo")
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for get_recipe_by_name

try:
    book.get_recipe_by_name(1)
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    book.get_recipe_by_name("")
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

print()

# Error cases for get_recipes_by_types

try:
    book.get_recipes_by_types(1)
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    book.get_recipes_by_types("")
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)

try:
    book.get_recipes_by_types("foo")
except AssertionError as e:
    print(f"AssertionError: {e}", file=stderr)
