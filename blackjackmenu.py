# Filename: blackjackmenu.py
# Author: Jaime Parra
# Date: November 25, 2021
# Program description: display menu choice for blackjack game with
#                      an exit choice

# Input: 



print("       \nWelcome to the Blckjack table\n       Good Luck!!! ")


menuChoice = 0

while menuChoice != 3:
    print("\n1) See rules\n2) Play game\n3) Exit")
    menuChoice = int(input("\nEnter your choice: "))

    if menuChoice == 1:
        print("\nThe rules of the game are.\n")
    elif menuChoice == 2:
        print("\nProceed to play the game.\n")
    elif menuChoice == 3:
        print("\nThanks for playing\nCome back soon :)\n")
    else:
        print("\nInvalid choice. you must choose between 1,2 or 3\n")
