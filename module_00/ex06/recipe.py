cookbook = {
    "Sandwich":{
        "ingredients":["ham","bread","cheese","tomatoes"],
        "meal":"lunch",
        "prep_time":10,
    },
    "Cake":{
        "ingredients":["flour","sugar","eggs"],
        "meal":"dessert",
        "prep_time":60,
    },
    "Salad":{
        "ingredients":["avocado","arugula","tomatoes","spinach"],
        "meal":"lunch",
        "prep_time":15,
    }
}
newInput=""
ingredients=[]
meal=""

def printAllNames():
    for var in cookbook:
        print(var)
def printRecipeDetails(name):
    if name in cookbook:
        for cle, valeur in cookbook[name].items():
            print("{} : {}.".format(cle, valeur))
    else:
        print("wrong recipe name")
def deleteRecipe(name):
    if name in cookbook:
        del cookbook[name]
def addRecipe(name, ingredients, meal, prep_time):
    if name not in cookbook:
        cookbook[name]={"ingredients":ingredients,meal:meal,prep_time:prep_time}

def getRecipeData():
    prep_time=0
    meal=""
    newInput=""
    name=input("Enter a name:\n")
    ingredients.append(input("Enter ingredients:\n"))
    newInput=input()
    ingredients.append(newInput)
    newInput=input()
    while newInput!="":
        ingredients.append(newInput)
        newInput=input()
    while meal=="":
        temp_meal=input("Enter a meal type:\n")
        try:
            int(temp_meal)
        except ValueError:
            meal=temp_meal
        if meal=="":
            print("Value isn't a string.")
    while prep_time<=0:
        try:
            prep_time=int(input("Enter a preparation time:\n"))
        except ValueError:
            print("Value has to be a positive integer.")
    addRecipe(name,ingredients,meal,prep_time)

def main():
    while 1:
        usr_choice=0
        while usr_choice==0:
            try:
                usr_choice=int(input("\nList of available option:\n1-Print CookBook\n2-Print Recipe\n3-Add Recipe\n4-Delete Recipe\n5-Quit\n"))
            except ValueError:
                print("Input need to be an Integer.")
                usr_choice=0
        print("")
        if usr_choice==1:
            printAllNames()
        elif usr_choice==2:
            printAllNames()
            name=input("Enter the name of the Recipe to get its details:\n")
            if name in cookbook:
                printRecipeDetails(name)
            else:
                print("Recipe not found.")
        elif usr_choice==3:
            getRecipeData()
        elif usr_choice==4:
            printAllNames()
            name=input("Enter the name of the Recipe you want to delete:\n")
            if name in cookbook:
                deleteRecipe(name)
            else:
                print("Recipe not found.")
        elif usr_choice==5:
            print("Cookbook closed. Goodbye !")
            exit()
        else:
            print("Invalid option.")

if __name__=='__main__':
    main()