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
#           2. Define print function
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
#                   card one is equal to dealCard function
#                   cardOne is removed from the list
#                   if receivedTotal is equal to or greater than 14
#                        sendTotal is equal to startTotal + cardOne
#                        return sendTotal
#                   else:
#                        randomly generated number is assigned to card two
#                        cardTwo is removed from the list
#                        totalCards is the sum of cardOne and cardTwo
#                        sendTotal is equal to receivedTotal + totalCards
#                        return sendTotal
#           6. Define ComputerTurn function
#                   if computer total is greater that 17 
#                           break from function
#                   randomly generated number is assigned to cardOne
#                   if computerTotal is greater than or equal to 14
#                          computerTotal is equal to computerTotal + cardOne
#                   elif computerTotal is less than 14 
#                         randomly generated number is assigned to card two
#                         totalCards is the sum of card one and card two 
#                         computerTotal is equal to computerTotal + totalCards


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
#                     deckCards is assigned to a list equal to 1 decks of cards 
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
def dealCard(card):
    pickCard = random.choice(card)
    return pickCard
def playerTurn(total, cards):
    cardOne = dealCard(cards)
    if total >= 14:
        total += cardOne
        return total, cardOne
    else:
        cardTwo = dealCard(cards)
        totalCards = cardOne + cardTwo
        total += totalCards
        return total, cardOne, cardTwo

def computerTurn(total, cards):
    if total >= 17:
        return
    cardOne = dealCard(cards)
    if total >= 14:
        total += cardOne
        return total, cardOne
    else:
        cardTwo = dealCard(cards)
        totalCards = cardOne + cardTwo
        total += totalCards
        return total, cardOne, cardTwo
def gameMenu(name):
    print(name + ", please choose one of the following""\n1) See rules\n2) Play game\n3) Exit")
    menuChoice = int(input("\nEnter your choice: "))
    while True:
        try:
            if menuChoice == 3:
                print("\nThank you for playing!")
                return 3
            while menuChoice != 3:
                while menuChoice == 1:
                    print("\nThe rules of the game are.\n")
                    menuChoice = int(input("\nEnter your choice: "))
                    if menuChoice == 3:
                        print("\nThank you for playing!")
                        return 3
                    elif menuChoice == 2:
                        return
                if menuChoice == 2:
                    print("\nProceed to play the game.\n")
                    return
                else:
                    print("\nInvalid choice. you must choose between 1,2 or 3\n")
        except:
            print("Error, please enter and integer")
        
def getUserName():
    userName = input("What is your name? ")
    print ("Hello, ", userName + "!")
    return userName
def hitOrStay():
    player1 = input("Do you want another card? Y/N:").upper()
    while True:
        try:   
            if player1 == "Y" or player1 == "YES":
                return True
            else:
                player1 == "N" or player1 == "NO"
                return False
        except:
            print("Error. Invalid Entry")

def determineWinLose(uTotal, cTotal, name, boolean):
    if uTotal > 21 and cTotal > 21:
        print("\nTie game!")
        gameMenu(name)
    if uTotal > 21:    
        print("\n" + name,"loses!")
        gameMenu(name)
    elif cTotal > 21:
        print("\n" + name,"wins!")
        gameMenu(name)
    elif uTotal == 21 and cTotal == 21:
        print("\n" + name,"and the computer tie!")
        gameMenu(name)
    elif uTotal == 21:
        print("\n" + "You hit 21!")
        print("\n" + name,"Wins!")
        gameMenu(name)
    elif cTotal == 21:
        print("\nThe computer hit 21!")
        print("\n" + name,"loses!")
        gameMenu(name)
    elif boolean == False:
        if uTotal > cTotal:
            print("\n" + name,"wins!")
            gameMenu(name)
        elif uTotal < cTotal:
            print("\n" + name,"loses!")
            gameMenu(name)
        elif uTotal == cTotal:
            print("\n" + name,"and the computer tie!")
            gameMenu(name)
    else:
        return

def print(fname):
    print(fname)
    time.sleep(.25)

def playAgain():
    while True:
        try:
            response = input("Would you like to play again (y/n)? :").lower()
            if response == "y":
                return True
            elif response == "n":
                print("\nThank you for playing!\n")
                print("\nGoodbye!\n")
                exit()
            
        except TypeError:
            print("Invalid response. Try again.")
        except ValueError:
            print("Invalid response. Try again.")
        except:
            print("Invalid response. Try again.")

def dealCard(card):
    pickCard = random.choice(card)
    return pickCard
def startGame(cards, name):
        userCard1 = dealCard(cards)
        userCard2 = dealCard(cards)
        userTotal = userCard1 + userCard2
        computerCard1 = dealCard(cards)
        computerCard2 = dealCard(cards)
        computerTotal = computerCard1 + computerCard2
        #Display user and computer totals
        print(name + "'s total is", userTotal) 
        print("Computer total:", computerTotal) 
        #Remove card rolls from cards list
        cards.remove(userCard1)
        cards.remove(userCard2)
        cards.remove(computerCard1)
        cards.remove(computerCard2)   
        return userCard1, userCard2, userTotal, computerCard1, computerCard2, computerTotal, cards




def main():

# Declare Variables
    userTotal = 0
    userName = getUserName()
    computerTotal = 0
    userChoice = True

    gameMenu(userName)

# deckCards is assigned to a list equal of 1 decks of cards 
    deckCards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

    userCard1, userCard2, userTotal, computerCard1, computerCard2, computerTotal, deckCards = startGame(deckCards, userName)

# determine if user or computer wins
    determineWinLose(userTotal, computerTotal, userName, userChoice) 

# hitOrStay function and return true or false
    userChoice = hitOrStay()

# if userChoice is true, user gets another card otherwise its the computers turn
    while userChoice == True:
        #Players turn and remove cards from deck
        userTotal, userCard1, userCard2 = playerTurn(userTotal, deckCards)
        deckCards.remove(userCard1)
        deckCards.remove(userCard2)
        # computerTurn function and remove cards from deck
        computerTotal, computerCard1, computerCard2 = computerTurn(computerTotal, deckCards)
        deckCards.remove(computerCard1)
        deckCards.remove(computerCard2)
# display player and computers New totals
        print("Your total is: " + str(userTotal))
        print("Computer total is: " + str(computerTotal))

# determineWinLoses function passing userTotal, computerTotal
        determineWinLose(userTotal, computerTotal, userName, userChoice)
        userChoice = hitOrStay()
#while computer total is less 17
    while computerTotal < 17:
        computerTotal = computerTurn(computerTotal, deckCards)
        determineWinLose(userTotal, computerTotal, userName, userChoice)
    determineWinLose(userTotal, computerTotal, userName, userChoice)

main()





###RULES###
###FOR INSTRUCTIONS###

#  The goal of the game is to score 21 points, or as near as possible without going over. The two players take turns dealing two cards as many times as desired and adding up the cards dealt on each round.

# A player who totals over 21 is bust and loses the game.

# The player whose total is nearest 21, after each player has had a turn, wins the game.

# In the case of an equality high total, the game is tied.
# The game is over at the end of a round when:

# One or both players are bust.
# Both players choose to stay.

# Once a player totals 14 or more, one of the cards is discarded for the consecutive turns.

# The house must deal the card until the total is 17 or higher. At 17 or higher, the house must stay.

# Project Requirements

# The program will start by prompting the user for the name of the player.

# The game will be implemented using a menu-driven interface that provides the following options: