from recipe import Recipe
from book import Book

tourte=Recipe("tourte",3,5,["farine","sel"],"une bonne tourte","lunch")
pain=Recipe("pain",5,10,["farine","sel","eau"],"du bon pain","lunch")
book=Book("list")
book.add_recipe(tourte)
book.add_recipe(pain)
# book.get_recipe_by_name("pain")
# book.get_recipe_by_name("tourte")
book.get_recipes_by_types("lunch")