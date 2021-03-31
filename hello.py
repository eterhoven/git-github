def start_game():

    game_on = True

    while game_on:

        x = input("Would you like to play? Y or N")
       
        if x.lower == 'y':
            print("We have succesfully started the game")
            game_on = False
        elif x.lower == 'n':
            print("Okay sure, we will leave that alone")
            game_on = False
        else:
            print("That was not a valid selection")

print("Welcome to the new python file")

start_game()

