from datetime import datetime
from recipe import Recipe
class Book:
    def __init__(self,name):
        err_return=["name"]
        def input_error(err_code):
            print("error: corrupted book setup value: "+err_return[err_code]+".")
            exit()
        self.name=name if isinstance(name,str)and name.isalpha()else input_error(0)
        self.creation_date=datetime.now()
        self.last_update=datetime.now()
        self.recipes_list={
            "starter":[],
            "lunch":[],
            "dessert":[],
        }
    def get_recipe_by_name(self,name):
        for rtype in self.recipes_list:
            for i in self.recipes_list[rtype]:
                if i.name==name:
                    print(i)
    def get_recipes_by_types(self,recipe_type):
        for rtype in self.recipes_list:
            if rtype==recipe_type:
                for i in self.recipes_list[rtype]:
                    print(i)
    def add_recipe(self,recipe):
        if not isinstance(recipe, Recipe):
            print("error: cannot add non-Recipe type to the book.")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update=datetime.now()
