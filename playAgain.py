#determine if user would like to play again
#ensure that the user enters a valid response
from printPause import printPause
def playAgain():
    while True:
        try:
            response = input("Would you like to play again (y/n)? :").lower()
            if response == "y":
                return True
            elif response == "n":
                printPause("\nThank you for playing!\n")
                exit()
            
        except TypeError:
            print("Invalid response. Try again.")
        else:
                print("Invalid response. Try again.")