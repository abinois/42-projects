from recipe import Recipe
from book  import Book

b = Book('The Mafaking Book')
r0 = Recipe('flan mireille', 'desert', 240, 5, ['lait', 'oeufs', 'sucre de canne', 'caramel'])
r1 = Recipe('flan nature', 'desert', 40, 1, ['lait', 'oeufs', 'sucre'], des='Faites le flan.')
r2 = Recipe('steack à la sauce', 'lunch', 30, 2, ['boeuf', 'poivre', 'beurre', 'sel'])
r0.add_description("Agitez le flan en tout sens jusqu'a satisfaction.")
b.add_recipe(r0)
b.add_recipe(r1)
b.add_recipe(r2)
print(b)
b.get_recipe_by_name('flan mireille')
b.get_recipes_by_types('gouter')
b.get_recipes_by_types('desert')

