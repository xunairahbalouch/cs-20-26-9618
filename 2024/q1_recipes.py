import csv
import os


class Recipe:
    """Task 1.1: Recipe class"""
    def __init__(self, recipe_id, name, cuisine, prep_time, cook_time, difficulty, servings):
        self.recipe_id = recipe_id
        self.name = name
        self.cuisine = cuisine
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.difficulty = difficulty
        self.servings = servings
    
    def total_time(self):
        return self.prep_time + self.cook_time
    
    def __str__(self):
        return (f"ID: {self.recipe_id}, Name: {self.name}, Cuisine: {self.cuisine}, "
                f"Prep: {self.prep_time}min, Cook: {self.cook_time}min, "
                f"Difficulty: {self.difficulty}, Servings: {self.servings}")


def LoadRecipes(filename="recipes.csv"):
    """Task 1.1: Load recipes from CSV file"""
    recipes = {}
    
    if not os.path.exists(filename):
        print(f"Error: {filename} not found")
        return recipes
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            recipe_id = row[0]
            recipes[recipe_id] = Recipe(
                row[0], row[1], row[2],
                int(row[3]), int(row[4]),
                row[5], int(row[6])
            )
    
    print(f"Loaded {len(recipes)} recipes")
    return recipes


def DisplayAllRecipes(recipes):
    """Task 1.1: Display all recipes"""
    print("\nAll Recipes:")
    for recipe in recipes.values():
        print(f"  {recipe}")


def DisplayRecipesByCuisine(cuisine, recipes):
    """Task 1.2: Display recipes by cuisine type"""
    found = []
    for recipe in recipes.values():
        if recipe.cuisine.lower() == cuisine.lower():
            found.append(recipe)
    
    if found:
        print(f"\n{cuisine} recipes:")
        for recipe in found:
            print(f"  {recipe}")
    else:
        print(f"No {cuisine} recipes found")
    
    return found


def DisplayRecipesByDifficulty(difficulty, recipes):
    """Task 1.2: Display recipes by difficulty level"""
    found = []
    for recipe in recipes.values():
        if recipe.difficulty.lower() == difficulty.lower():
            found.append(recipe)
    
    if found:
        print(f"\n{difficulty} recipes:")
        for recipe in found:
            print(f"  {recipe}")
    else:
        print(f"No {difficulty} recipes found")
    
    return found


def DisplayRecipesByTotalTime(max_time, recipes):
    """Task 1.2: Display recipes that can be made within max_time"""
    found = []
    for recipe in recipes.values():
        if recipe.total_time() <= max_time:
            found.append(recipe)
    
    if found:
        print(f"\nRecipes under {max_time} minutes total:")
        for recipe in found:
            print(f"  {recipe.name}: {recipe.total_time()} minutes")
    else:
        print(f"No recipes found under {max_time} minutes")
    
    return found


def SearchRecipesByName(search_term, recipes):
    """Task 1.2: Search recipes by name (partial match)"""
    found = []
    search_lower = search_term.lower()
    
    for recipe in recipes.values():
        if search_lower in recipe.name.lower():
            found.append(recipe)
    
    if found:
        print(f"\nRecipes matching '{search_term}':")
        for recipe in found:
            print(f"  {recipe}")
    else:
        print(f"No recipes found matching '{search_term}'")
    
    return found


def AddNewRecipe(recipe_id, name, cuisine, prep_time, cook_time, difficulty, servings, recipes):
    """Task 1.3: Add a new recipe"""
    if recipe_id in recipes:
        print(f"Recipe ID {recipe_id} already exists")
        return False
    
    recipes[recipe_id] = Recipe(recipe_id, name, cuisine, prep_time, cook_time, difficulty, servings)
    print(f"Added recipe: {name}")
    return True


def UpdateRecipeTimes(recipe_id, prep_time=None, cook_time=None, recipes=None):
    """Task 1.3: Update recipe times"""
    if recipe_id not in recipes:
        print(f"Recipe {recipe_id} not found")
        return False
    
    if prep_time is not None:
        recipes[recipe_id].prep_time = prep_time
    if cook_time is not None:
        recipes[recipe_id].cook_time = cook_time
    
    print(f"Updated {recipes[recipe_id].name}")
    return True


def UpdateRecipeDifficulty(recipe_id, difficulty, recipes):
    """Task 1.3: Update recipe difficulty"""
    if recipe_id not in recipes:
        print(f"Recipe {recipe_id} not found")
        return False
    
    recipes[recipe_id].difficulty = difficulty
    print(f"Updated {recipes[recipe_id].name} difficulty to {difficulty}")
    return True


def DeleteRecipe(recipe_id, recipes):
    """Task 1.3: Delete a recipe"""
    if recipe_id in recipes:
        removed = recipes.pop(recipe_id)
        print(f"Deleted recipe: {removed.name}")
        return True
    
    print(f"Recipe {recipe_id} not found")
    return False


def SaveRecipes(filename, recipes):
    """Task 1.4: Save all recipes to CSV file"""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["RecipeID", "Name", "Cuisine", "PrepTime", "CookTime", "Difficulty", "Servings"])
        
        for recipe in recipes.values():
            writer.writerow([recipe.recipe_id, recipe.name, recipe.cuisine,
                           recipe.prep_time, recipe.cook_time,
                           recipe.difficulty, recipe.servings])
    
    print(f"Saved {len(recipes)} recipes to {filename}")


def CalculateAverageTimes(recipes):
    """Task 1.4: Calculate average prep and cook times"""
    if not recipes:
        return 0, 0
    
    total_prep = sum(r.prep_time for r in recipes.values())
    total_cook = sum(r.cook_time for r in recipes.values())
    
    avg_prep = total_prep / len(recipes)
    avg_cook = total_cook / len(recipes)
    
    print(f"Average prep time: {avg_prep:.1f} minutes")
    print(f"Average cook time: {avg_cook:.1f} minutes")
    
    return avg_prep, avg_cook


def GetRecipesByCuisine(recipes):
    """Task 1.4: Get recipes grouped by cuisine"""
    cuisines = {}
    
    for recipe in recipes.values():
        if recipe.cuisine not in cuisines:
            cuisines[recipe.cuisine] = []
        cuisines[recipe.cuisine].append(recipe)
    
    for cuisine, recipe_list in cuisines.items():
        print(f"\n{cuisine}: {len(recipe_list)} recipes")
        for recipe in recipe_list:
            print(f"  - {recipe.name} ({recipe.difficulty})")
    
    return cuisines


def FindQuickestRecipes(n, recipes):
    """Task 1.4: Find n quickest recipes by total time"""
    sorted_recipes = sorted(recipes.values(), key=lambda r: r.total_time())
    quickest = sorted_recipes[:n]
    
    print(f"\nTop {n} quickest recipes:")
    for recipe in quickest:
        print(f"  {recipe.name}: {recipe.total_time()} minutes total")
    
    return quickest


def FindRecipesForServings(servings, recipes):
    """Task 1.4: Find recipes suitable for serving count"""
    found = []
    for recipe in recipes.values():
        if recipe.servings >= servings:
            found.append(recipe)
    
    if found:
        print(f"\nRecipes for at least {servings} servings:")
        for recipe in found:
            print(f"  {recipe.name}: serves {recipe.servings}")
    else:
        print(f"No recipes found for {servings} servings")
    
    return found


if __name__ == "__main__":
    recipes = LoadRecipes("recipes.csv")
    
    if recipes:
        DisplayAllRecipes(recipes)
        
        print("\n" + "=" * 80)
        print("Task 1.2: Search and Filter")
        print("=" * 80)
        DisplayRecipesByCuisine("Italian", recipes)
        DisplayRecipesByDifficulty("Easy", recipes)
        DisplayRecipesByTotalTime(60, recipes)
