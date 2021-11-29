#Program Name: vingtEtUn.py
#Authors: Jaime Parra Velez, Marjorie Gilles, Corey Duke
#Date: 11/23/2021
#Program Description: Game of 21 where the user can choose to hit or stay and wins if they get a higher score than the computer.

#input: import random module, import time module, menu choice, and user input, 
#Processing:1. Define gameMenu function
#                  Display game menu
#                  Try to get user selection
#                      If user selection is 1
#                               Return 1
#                      If user selection is 2
#                               Return 2
#                      If user selection is 3
#                               Return 3
#                  If user selection is invalid, display error message and try again
#           2. Define printPause function
#                   Display message
#                   Pause before next message
#           3. Define getUserName function
#                  userOne = input user name prompt
#                  return userOne
#           4. Define hitOrStay function
#                  prompt userOne to hit or stay prompt
#                  if user input is invalid, display error message and try again
#                  if user input equals hit 
#                        return True
#                  elif user input equals stay
#                        return False 
#           5. Define playerTurn function
#                   if userChoice equals false
#                        break from function
#                   dice one is equal to diceRoll function
#                   diceOne is removed from the list
#                   if receivedTotal is equal to or greater than 14
#                        sendTotal is equal to startTotal + diceOne
#                        return sendTotal
#                   else:
#                        randomly generated number is assigned to dice two
#                        diceTwo is removed from the list
#                        totalRoll is the sum of diceOne and diceTwo
#                        sendTotal is equal to receivedTotal + totalRoll
#                        return sendTotal
#           6. Define ComputerTurn function
#                   if computer total is greater that 17 
#                           break from function
#                   randomly generated number is assigned to diceOne
#                   if computerTotal is greater than or equal to 14
#                          computerTotal is equal to computerTotal + diceOne
#                   elif computerTotal is less than 14 
#                         randomly generated number is assigned to dice two
#                         totalRoll is the sum of dice one and dice two 
#                         computerTotal is equal to computerTotal + totalRoll


#           7. Define determineWinLoss function
#               if userTotal is greater than 21
#                  Display userName loses 
#                  gameMenu is called
#               elif computerTotal is greater than 21
#                  Display userName wins
#                  gameMenu is called
#               elif usertotal is equal to 21 and computerTotal is equal to 21
#                  Display userName and computerName tie
#                  gameMenu is called
#               elif userTotal is equal to 21
#                  Display userName wins
#                  gameMenu is called
#               elif computerTotal is equal to 21
#                  Display Computer hit 21
#                  Display userName loses
#                  gameMenu is called
#               if userInput equals stay and computerTotal is greater than 17
#                       If userTotal is greater than computerTotal
#                               Display userName wins
#                               gameMenu is called
#                       If userTotal is less than computerTotal
#                               Display userName loses
#                               gameMenu is called
#                       If userTotal is equal to computerTotal
#                               Display userName and computerName tie
#                               gameMenu is called
#              Else:
#                    break from function


#           9. Define main function 
#                     Declare userTotal and computerTotal as 0
#                     Declare userName as empty string
#                     Go to game menu function
#                         Return Choice
#                     numberSet is assigned to a list equal to 1 decks of cards 
#                     If choice is 1
#                          enter gameRules function
#                     Else if choice is 2
#                           determineWinLoss function passing userTotal, computerTotal
#                                 hitOrStay function
#                                 While user input is not equal to stay 
#                                       playerTurn function with userTotal as parameter
#                                       computerTurn function with computerTotal as parameter
#                                       display player and computers New totals
#                                       determineWinLoss function passing userTotal, computerTotal
#                                       hitOrStay function
#                                 While computer total is less 17
#                                       computerTurn function with computerTotal as parameter
#                                       determineWinLoss function passing userTotal, computerTotal
#                     Else if choice is 3
#                          Exit the game with a message
#
#           10. Define gameRules function
#                     Display game rules
#
#           11. Define playAgain function
#                     try to prompt user to play again
#                             if user input equals yes
#                                   return True
#                             elif user input equals no
#                                   display exit message
#                                   exit program    
#                     if user input is invalid, display error message and try again
#output:

import random
import time

def playerTurn():

def computerTurn():

def gameMenu():

def getUserName():

def hitOrStay():
  
def gameRules():

def determineWinLoss(userTotal, computerTotal):

def printPause(fname):
    print(fname)
    time.sleep(.25)

def playAgain():
    while True:
        try:
            response = input("Would you like to play again (y/n)? :").lower()
            if response == "y":
                return True
            elif response == "n":
                printPause("\nThank you for playing!\n")
                printPause("\nGoodbye!\n")
                exit()
            
        except TypeError:
            print("Invalid response. Try again.")
        except ValueError:
            print("Invalid response. Try again.")
        except:
            print("Invalid response. Try again.")

def diceRoll(dice):
    rollDice = random.choice(dice)
    return rollDice
#Define main function 
def main():
    print("Let's Begin Playing Vingt-Et-Un!")
# Declare Variables
    userTotal = 0
    userName = getUserName()
    computerTotal = 0
    userChoice = 0

# Go to game menu function
    choice = gameMenu()

# numberSet is assigned to a list equal to 1 decks of cards 
    numberSet = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

# Determine choices and perform actions related to choices
    if choice == 1:
        gameRules()
    elif choice == 2:
    #Game starts with initial rolls
        userDice1 = diceRoll(numberSet)
        numberSet.remove(userDice1)
        userDice2 = diceRoll(numberSet)
        numberSet.remove(userDice2)
        userTotal = userDice1 + userDice2
        computerDice1 = diceRoll(numberSet)
        numberSet.remove(computerDice1)
        computerDice2 = diceRoll(numberSet)
        numberSet.remove(computerDice2)
        computerTotal = computerDice1 + computerDice2
        #Display user and computer totals
        print(userName + "'s total is", userTotal) 
        print("Computer total:", computerTotal)

# determineWinLoss function passing userTotal, computerTotal
        determineWinLoses(userTotal, computerTotal)

# hitOrStay function
        hitStay = hitOrStay()

# While user input is not equal to stay
        while hitStay == True

# playerTurn function with userTotal as parameter
            userTotal = playerTurn(userTotal)

# computerTurn function with computerTotal as parameter
            computerTotal = computerTurn(computerTotal)

# display player and computers New totals
            printPause("Your total is: " + str(userTotal))
            printPause("Computer total is: " + str(computerTotal))

# determineWinLoses function passing userTotal, computerTotal
            determineWinLoses(userTotal, computerTotal)
            hitStay = hitOrStay()
#while computer total is less 17
        while computerTotal < 17:
            computerTotal = computerTurn(computerTotal)
            determineWinLoses(userTotal, computerTotal)



###RULES###
###FOR INSTRUCTIONS###

#  The goal of the game is to score 21 points, or as near as possible without going over. The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.

# A player who totals over 21 is bust and loses the game.

# The player whose total is nearest 21, after each player has had a turn, wins the game.

# In the case of an equality high total, the game is tied.
# The game is over at the end of a round when:

# One or both players are bust.
# Both players choose to stay.

# Once a player totals 14 or more, one of the dies is discarded for the consecutive turns.

# The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.

# Project Requirements
# The program will start by prompting the user for the name of the player.

# The game will be implemented using a menu-driven interface that provides the following options: