import re

class recette():

    def __init__(self, meal, prep_time, liste):
        self.meal = meal
        self.prep_time = prep_time
        self.ingredients = liste
        self.recipe = "Cuisinez les ingrédients et voilà."
     
    def aff_recipe(self):
        print("Recipe for {}:".format(self.meal))
        print("Ingredients list: {}".format(self.ingredients))
        print(self.recipe)
        print("Takes {} minutes of cooking.\n".format(self.prep_time))

cookbook = {
    'sandwich':recette('sandwich', 5, ['ham', 'bread', 'cheese', 'tomatoes']),
    'cake':recette('cake', 40, ['flour', 'sugar', 'egg']),
    'salad':recette('salad', 15, ['salad', 'verte']) }

def f1():
    name = input("Please enter the recipe's name:").strip()
    time = input("Please enter the recipe's preparation time:").strip()
    print("Please enter the recipe's ingredients:")
    ingredients = re.sub(r'\s+', ' ', input().strip()).split(' ')
    new = recette(name, time, ingredients)
    cookbook[name] = new

def f2():
    name = input("To delete, please enter the recipe's name:\n").strip()
    if name in cookbook:
        cookbook.pop(name)
    else:
        print("This recipe remain unknown as we speak.")

def f3():
    name = input("Please enter the recipe's name to get its details:").strip()
    if name in cookbook:
        cookbook[name].aff_recipe()
    else:
        print("This recipe remain unknown as we speak.")

def f4():
    for name, recipe in cookbook.items():
        recipe.aff_recipe()

function = {
    '1':f1,
    '2':f2,
    '3':f3,
    '4':f4,
    '5':lambda: exit("Cookbook closed.") }

if __name__ == '__main__':
    while(1):
        print("Please select an option by typing the corresponding number:")
        print(" - 1: Add a recipe", " - 2: Delete a recipe", " - 3: Print a recipe", " - 4: Print the cookbook", " - 5: Quit", sep='\n')
        choice = input().strip()
        if choice in function:
            function[choice]()
        elif choice != '':
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")