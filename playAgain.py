#determine if user would like to play again
#ensure that the user enters a valid response
from DisplayPause import DisplayPause
def playAgain():
    while True:
        try:
            response = input("Would you like to play again (y/n)? :").lower()
            if response == "y":
                return True
            elif response == "n":
                DisplayPause("\nThank you for playing!\n")
                exit()
            
        except TypeError:
            Display("Invalid response. Try again.")
        except ValueError:
            Display("Invalid response. Try again.")
        except:
            Display("Invalid response. Try again.")
