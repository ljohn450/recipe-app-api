import json

# Recipe repository database (stored in a JSON file)
RECIPE_FILE = "recipes.json"

def load_recipes():
    """Load recipes from JSON file."""
    try:
        with open(RECIPE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_recipes(recipes):
    """Save recipes to JSON file."""
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

def add_recipe(name, ingredients, instructions):
    """Add a new recipe to the repository."""
    recipes = load_recipes()
    recipes[name] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes(recipes)
    print(f"Recipe '{name}' added successfully!")

def view_recipes():
    """Display all recipes."""
    recipes = load_recipes()
    if recipes:
        for name, details in recipes.items():
            print(f"\nRecipe: {name}")
            print(f"Ingredients: {', '.join(details['ingredients'])}")
            print(f"Instructions: {details['instructions']}")
    else:
        print("No recipes found!")

def search_recipe(name):
    """Search for a recipe by name."""
    recipes = load_recipes()
    if name in recipes:
        details = recipes[name]
        print(f"\nRecipe: {name}")
        print(f"Ingredients: {', '.join(details['ingredients'])}")
        print(f"Instructions: {details['instructions']}")
    else:
        print(f"Recipe '{name}' not found!")

# Sample execution
if __name__ == "__main__":
    add_recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "cheese", "bacon"], "Cook pasta, mix with eggs, cheese, and bacon.")
    view_recipes()
    search_recipe("Spaghetti Carbonara")
