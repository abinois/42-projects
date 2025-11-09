import datetime
from recipe import Recipe

class Book():
    """Livre de recettes"""
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.last_update = self.creation_date
        self.recipe_list = {'starter':{}, 'lunch':{}, 'desert':{}}

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self.name.center(25, '_') + "\n"
        for categorie, liste in self.recipe_list.items():
            txt += categorie + ":\n\t" + " | ".join(liste.keys()) + "\n"
        txt += "\n".rjust(26, '_')
        return(txt)

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for categorie, liste in self.recipe_list.items():
            if name in liste:
                liste[name].info()
                break
        print("This recipe is not in the book.")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipe_list:
            print("Recipes for", recipe_type, ":", end=' ')
            print(" | ".join(self.recipe_list[recipe_type].keys()))
        else:
            print("This type of recipe is not in the book.")


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            exit("This is not an instance of Recipe.")
        self.recipe_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")