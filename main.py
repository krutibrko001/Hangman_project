# Hangman
from random import choice
import art
import sys



word_list = ["Hello", "Hi", "Fun", "God", "Happy", "Python", "is", "the", "Best"]

# Setting up the CONSTANTS.
print("Type (exit) to quit!")
SECRET_WORD = choice(word_list).lower()
DASH = "-"
LST = []
D_LIST = []
GAME_ON = True
LIVES = len(SECRET_WORD)

#TODO - Welcoming msg
#TODO - implement lives
#TODO - show number of character to the screen.
#TODO - ask to type exit - to quit.





def start():
    global GAME_ON
    global LIVES
    
    for item in SECRET_WORD:
        LST.append(item)
        D_LIST.append(DASH)

    # Display dash w-o-r-d.
    print(D_LIST)

    while GAME_ON:
        # Check for life's
        if LIVES == 0:
            print(f"Out of tries. You have {LIVES} lives.")
            GAME_ON = False

        # check for word.
        finall = "".join(D_LIST)
        if finall == SECRET_WORD:
            print("Congratulations! You have WON!")
            break
        
        usr_input = input("Guess a character: ")
        # Check if user wants to quit?
        if usr_input == "exit":
            print("Exiting... Goodbay!")
            sys.exit()

        if usr_input in LST:
            index = LST.index(usr_input)
            try:
                if usr_input in D_LIST:
                    D_LIST[index+1] = usr_input
            except IndexError:
                print("Character already in the list. Try other one!")
                continue
            else:
                D_LIST[index] = usr_input
            print(D_LIST)
        else:
            print("Sorry! Your character is not in the list.")
            LIVES -= 1

start()
