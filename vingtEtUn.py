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
#           2. Define DisplayPause function
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
#                   randomly generated number is assigned to diceOne
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
#                   randomly generated number is assigned to diceoOne
#                   if computerTotal is greater than or equal to 14
#                          computerTotal is equal to computerTotal + diceOne
#                   elif computerTotal is less than 14 
#                         randomly generated number is assigned to dice two
#                         totalRoll is the sum of dice one and dice two 
#                         computerTotal is equal to computerTotal + totalRoll
                        NEEDS WORK
#           7. Define determineWinLoss function
#               if userTotal is greater than 21
#                  Display userName loses 
#                  
#               elif computerTotal is greater than 21
#                  Display userName wins
#               elif usertotal is equal to 21 and computerTotal is equal to 21
#                  Display userName and computerName tie
#               elif userTotal is equal to 21
#                  Display userName wins
#               elif computerTotal is equal to 21
#                  Display Computer hit 21
#                  Display user loses
#               

                  
                        NEEDS WORK
#           8. Define Main function 
#                     Go into a loop of rounds where player & house will take turns throwing the dice.
#                     At each turn the system will ask the player/house whether to stay or roll.
#                     While userOne is not stay or user One is not bust and computer is not stay or computer is not bust
#                           If the house has a running total of 17 or higher, it stays, and the turn passes to the player.
#                           If the player/house option is to roll, the program simulates the roll of the two dies and updates & displays the player’s running total.
#                     If the player/house starts the round with an accumulated total of 14 points or more, only one die will be rolled.
#                     Once the game is over the system will display the result
#                     Winner
#                     Loser
#                     Tie]
                        NEEDS WORK
#           9. Define main function 
#                     Declare userTotal and computerTotal as 0
#                     Declare userName as empty string
#                     Display game menu 
#                         Return Choice
#                     numberSet is assigned to a list equal to 1 decks of cards 
#                     If choice is 1
#                          enter gameRules function
#                     Else if choice is 2
#                           Deal first two cards to player and computer
#                                 Cards are removed from the list
#                           determineWinLoss function
#                           Display player and computer cards
#                                 hitOrStay function
#                                 While user input is not equal to stay
#                                       playerTurn function with userTotal as parameter
#                                       computerTurn function with computerTotal as parameter
#                                       display player and computers New totals
#                                       hitOrStay function
#
#
#                           
#                           
#                     Else if choice is 3
#                          Exit the game with a message
#









#           10. Define gameRules function
#                     Display game rules
#           11. Define playAgain function
#                     try to prompt user to play again
#                             if user input equals yes
#                                   numberSet is set back to original values
#                                   return numberSet
#                             elif user input equals no
#                                   display exit message
#                                   exit program    
#                     if user input is invalid, display error message and try again
#output:

import random
from playAgain  import playAgain
from DisplayPause import DisplayPause
from gameRules import gameRules
from getUserName import getUserName
from hitOrStay import hitOrStay
from rollDice import rollDice
from computerTurn import computerTurn
from calculateScore import calculateScore
from gameMenu import gameMenu







































###List of numbers to be used in the game equal to two decks of cards###
numberSet = [,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

###roll dice then remove from list###
diceRoll = random.choice(numberSet)
numberSet.remove(diceRoll)



# Project Requirements
# The program will start by prompting the user for the name of the player.

# The game will be implemented using a menu-driven interface that provides the following options:

# 1. See the Rules.
# 2. Play Vingt-et-un.
# 3. Quit.
# If the user chooses 1 from the menu, display the rules of the game.

# If the user chooses 2 from the menu

# Go into a loop of rounds where player & house will take turns      throwing the dice.

# At each turn the system will ask the player/house whether to stay or roll.

# If the house has a running total of 17 or higher, it stays, and the turn passes to the player.
# If the player/house option is to roll, the program simulates the roll of the two dies and updates & displays the player’s running total.
# If the player/house starts the round with an accumulated total of 14 points or more, only one die will be rolled.
# Once the game is over the system will display the result

# Winner
# Loser
# Tie


# If the user chooses 3 from the menu, display a good-bye message and quit.

# The users can play the game as many times as they wish until they choose 3 to Quit














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