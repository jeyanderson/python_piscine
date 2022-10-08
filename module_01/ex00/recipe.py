
class Recipe:

    def __init__(self,name,cooking_lvl,cooking_time,ingredients,description,recipe_type):
        err_return=["name","cooking_lvl","cooking_time","ingredients","description","recipe_type"]
        def input_error(err_code):
            print("erorr: corrupted recipe setup value: "+err_return[err_code]+".")
            exit()
        self.name=name if isinstance(name,str)and name.isalpha()else input_error(0)
        self.cooking_lvl=cooking_lvl if isinstance(cooking_lvl,int)and(cooking_lvl>0&cooking_lvl<6)else input_error(1)
        self.cooking_time=cooking_time if isinstance(cooking_time,int)and cooking_time>0 else input_error(2)
        if isinstance(ingredients,list):
            for ingredient in ingredients:
                if not isinstance(ingredient,str)and ingredient.isalpha():
                    input_error(3)
        else:
            input_error(3)
        self.ingredients=ingredients
        self.description=description if (isinstance(description,str)and all(x.isalpha() or x.isspace() for x in description))or description==""else input_error(4)
        self.recipe_type=recipe_type if isinstance(recipe_type,str)and recipe_type.isalpha()and(recipe_type=="lunch"or recipe_type=="starter"or recipe_type=="dessert")else input_error(5)
    def __str__(self):
        txt=f"{self.name.capitalize()} recipe:\n\nCooking level: {self.cooking_lvl}\nCooking time: {self.cooking_time}\nIngredietns: {self.ingredients}\nDescription: {self.description}\nRecipe time: {self.recipe_type}"
        return txt