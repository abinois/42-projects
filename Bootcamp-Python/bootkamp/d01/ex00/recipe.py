from sys import exit

class Recipe():
    """Recette de cuisine"""
    def __init__(self, name, r_type, c_time, lvl, liste, des="Cuisinez les ingrédients et voilà."):
        try:
            self.name = name
            if r_type not in ('starter', 'lunch', 'desert'):
                exit(name + " : Recipe type unknown. Please choose between 'starter', 'lunch' or 'desert'.")
            self.recipe_type = r_type
            if not lvl in range(1, 6):
                exit(name + " : Cooking level must be between 1 and 5.")
            self.cooking_lvl = int(lvl)
            self.cooking_time = int(c_time)
            for ing in liste:
                if type(ing) is not str:
                    exit(name + " : Ingredients must be a list of string.")
            self.ingredients = liste
            if type(des) is not str:
                exit(name + " : Description must be of type str.")
            self.description = des
        except ValueError:
            exit(name + ' : Error in recipe instanciation. Expected int.')

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe for " + self.name + ":\n" + \
            "Difficulty : " + str(self.cooking_lvl) + "/5\n" + \
            "Takes " + str(self.cooking_time) + " min.\n" + \
            "Ingredients : " + str(self.ingredients) + "\n" + self.description + "\n"
        return txt
        
    def info(self):
        print(self)

    def add_description(self, description):
        """Add description to the recipe"""
        if type(description) is not str:
            exit("STR type object is expected for the recipe's description.")
        self.description = description
