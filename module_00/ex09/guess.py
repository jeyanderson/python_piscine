from random import randint

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGoodLuck!\n\n")
toguess=randint(1,100)
i = 1
while 1:
    usr_guess=input("What's your guess between 1 and 99?\n>> ")
    if not usr_guess.isdigit():
        if usr_guess!="exit":
            print("Value isnt an Integer.")
        else:
            print("Goodbye!")
            exit()
    else:
        usr_guess=int(usr_guess)
        if usr_guess==toguess:
            if toguess==42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            to_print="Congratulations, You've got it!\nYou won in "+str(i)+" attempts!"if i!=1 else"Congratulations, You've got it on your first try!"
            print(to_print)
            exit()
        to_print="Too low!"if usr_guess<toguess else"Too high!"
        print(to_print)
        i+=1