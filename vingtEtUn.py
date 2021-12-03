#Program Name: vingtEtUn.py
#Authors: Jaime Parra Velez, Marjorie Gilles, Corey Duke
#Date: 11/23/2021
#Program Description: Game of 21 where the user can choose to hit or stay and wins if they get a higher score than the computer.

#input: import random module, import time module, import sys, menu choice, and user input, 
#Processing:1. Define gameMenu function
#                  Display game menu and choices
#                  While True
#                      Try
#                        menuChoice equals user input
#                        if menuChoice equals 3
#                           display Thank you for playing! and exit
#                        while menuChoice not equal to 3
#                            while menuChoice equals 1
#                               display with gameRules function
#                               menuChoice equals user input
#                               if menuChoice equals 3
#                                   display Thank you for playing! and exit
#                                   return 3
#                               elif menuChoice equals 2
#                                   Return
#                           If user selection is 2
#                               Return 
#                           else:
#                               menuChoice equals user input
#                       Except if user selection is invalid, display error message and try again
#                             loop until user selection is valid
#                       Display invalid input message and try again
#           2. Define print function
#                   Display message
#                   Pause before next message
#           3. Define getUserName function
#                  userOne equals input user name prompt
#                  display Hello, userOne
#                  return userOne
#           4. Define hitOrStay function
#                  prompt userOne to hit or stay prompt
#                  while True
#                      Try
#                           if user input equals y or yes
#                               return hit
#                           else if user input equals n or no
#                               return stay
#                      except
#                           repeat loop
#                      display invalid input message and try again
#           5. Define playerTurn function
#                   card one is equal to dealCard function and cards is equal to cards
#                   if receivedTotal is equal to or greater than 14
#                        sendTotal is equal to startTotal + cardOne
#                        display new total
#                        return sendTotal and cards
#                   else:
#                        dealCard is assigned to card two and cards is equal to cards
#                        totalCards is the sum of cardOne and cardTwo
#                        sendTotal is equal to receivedTotal + totalCards
#                        display new total
#                        return sendTotal
#           6. Define ComputerTurn function
#                   if computer total is greater that 17 
#                        display computer stays with a total of computer total
#                        return total and cards
#                   cardOne is equal to dealCard function and cards is equal to cards
#                   if computerTotal is greater than or equal to 14
#                          computerTotal is equal to computerTotal + cardOne
#                          display computer new total
#                          return computerTotal and cards
#                   else
#                        cardTwo is equal to dealCard function and cards is equal to cards
#                        totalCards is the sum of card one and card two 
#                        computerTotal is equal to computerTotal + totalCards
#                        display computer new total
#                        return computerTotal and cards
#           7. Define determineWinLoss function
#               if computerTotal is greater than 21 and userTotal is greater than 21
#                   display tie
#                   play again?
#               if userTotal is greater than 21
#                  Display userName loses 
#                  Play Again?
#               elif computerTotal is greater than 21
#                  Display userName wins
#                  Play Again?
#               elif usertotal is equal to 21 and computerTotal is equal to 21
#                  Display userName and computerName tie
#                  Play Again?
#               elif userTotal is equal to 21
#                  Display userName wins
#                  Play Again?
#               elif computerTotal is equal to 21
#                  Display Computer hit 21
#                  Display userName loses
#                  Play Again?
#               if userInput equals stay and computerTotal is greater than or equal to 17
#                       If userTotal is greater than computerTotal
#                               Display userName wins
#                               Play Again?
#                       If userTotal is less than computerTotal
#                               Display userName loses
#                               Play Again?
#                       If userTotal is equal to computerTotal
#                               Display userName and computerName tie
#                               Play Again?
#              Else:
#                    break from function
#           8. Define gameRules function
#                   Display game rules
#           9. Define playAgain function
#                    set response variable to 0
#                    while response is equal not equal y or yes or n or no
#                         try
#                              response equals user input
#                              if response equals y or yes
#                                   go to main
#                              elif response equals n or no
#                                   exit
#                         except
#                              display invalid input message and try again
#                              loop until user input is valid
#           10. Define dealCard function
#                   pickCard is equal to random choice from deck of cards 
#                   remove the card from the deck
#                   return pickCard and deck with the card removed  
#           11. Define startGame function
#               userCard1, cards equals dealCard with cards
#               userCard2, cards equals dealCard with cards
#               userTotal is equal to userCard1 plus userCard2
#               computerCard1, cards equals dealCard with cards
#               computerCard2, cards equals dealCard with cards
#               computerTotal is equal to computerCard1 plus computerCard2
#               Display welcome message
#               Display userName and userTotal
#               Display computerName and computerTotal
#               return userTotal, computerTotal, cards
#           12. Define main function 
#                     Display Welcome message
#                     Declare userTotal and computerTotal as 0
#                     Prompt for userName
#                     userChoice equals True
#                     Go to game menu function
#                           returns if play game or quit is chosen
#                     if userChoice equals quit
#                           display Thank you for playing!
#                           exit
#                     deckCards is assigned to a list equal to 1 decks of cards with 6 as the highest card
#                     Start the game expecting userTotal, computerTotal, and deckCards(with dealt cards removed) returned.
#                     determineWinLoss function passing userTotal, computerTotal, userName, and userChoice
#                     prompt user with hitOrStay function
#                              While user input is equal to hit 
#                                    playerTurn function with userTotal as parameter
#                                    computerTurn function with computerTotal as parameter
#                                    display player and computers New totals
#                                    determineWinLoss function passing userTotal, computerTotal, userName, and userChoice
#                                    prompt user with hitOrStay function
#                              While computer total is less 17
#                                    computerTurn function with computerTotal as parameter
#                                    determineWinLoss function passing userTotal, computerTotal, userName, and userChoice
#                     determineWinLoss function passing userTotal, computerTotal, userName, and userChoice
#output:game rules, userName, userTotal, computerTotal, winLoss message, play again prompt, and exit message



#Import Modules
import random
import time
import sys




  #Display Game menu with 3 options and exception handling
def gameMenu(name):
    print(name + ", please choose one of the following""\n--------------------------------------\n1) See rules\n2) Play game\n3) Exit")
    while True:
        try:
            menuChoice = int(input("\nEnter your choice: "))
            if menuChoice == 3:
                print("\nThank you for playing!")
                return 3
            while menuChoice != 3:
                while menuChoice == 1:
                    gameRules()
                    menuChoice = int(input("\nEnter your choice: "))
                    if menuChoice == 3:
                        print("\nThank you for playing!")
                        return 3
                    elif menuChoice == 2:
                        return
                if menuChoice == 2:
                    return
                else:
                    menuChoice = input("\nInvalid choice. you must choose between 1,2 or 3\n")
        except:    
            pass
        print('\nIncorrect input, try again')




#add a pause to the print function
def printPause(string):
    print(string)
    time.sleep(.3)




#Prompt user to input their name
def getUserName():
    userName = input("What is your name? ")
    print("Hello,", userName + "!")
    return userName




#Determine if the user wants another card or not with exception handling
def hitOrStay():
    player1 = input("Do you want another card? y/n:").upper()
    while True:
        try:   
            if player1 == "Y" or player1 == "YES":
                return "hit"
            else:
                player1 == "N" or player1 == "NO"
                return "stay"
        except:
            pass
        print("\nInvalid input, try again")




#players turn then returns the total after the turn
def playerTurn(total, cards, name):
    cardOne, cards = dealCard(cards)
    if total >= 14:
        total += cardOne
        printPause("-----------------------------------")
        printPause("")
        print(name + "'s new total is " + str(total))
        print("")
        return total, cards
    else:
        cardTwo, cards = dealCard(cards)
        totalCards = cardOne + cardTwo
        total += totalCards
        printPause("-----------------------------------")
        printPause("")
        print(name + "'s new total is " + str(total))
        print("")
        return total, cards




#Determine if computer goes again then calculate the turn and return the total
def computerTurn(total, cards):
    if total >= 17:
        print("Computer stays with a total of " + str(total) + "\n")
        return total, cards
    cardOne, cards = dealCard(cards)
    if total >= 14:
        total += cardOne
        printPause("-----------------------------------")
        printPause("")
        print("The Dealer's new total is " + str(total))
        print("")
        return total, cards
    else:
        cardTwo, cards = dealCard(cards)
        totalCards = cardOne + cardTwo
        total += totalCards
        printPause("-----------------------------------")
        printPause("")
        print("The Dealer's new total is " + str(total))
        print("")
        return total, cards

        


#Goes through the user and computers totals and determines who wins, ties, loses, or if the game is still going
def determineWinLose(uTotal, cTotal, name, hitPass):
    if uTotal > 21 and cTotal > 21:
        print("\nTie game!\n")
        playAgain()
    elif uTotal > 21:    
        print("\n" + name,"loses!\n")
        playAgain()
    elif cTotal > 21:
        print("\n" + name,"wins!\n")
        playAgain()
    elif uTotal == 21 and cTotal == 21:
        print("\n" + name,"and the computer tie!\n")
        playAgain()
    elif uTotal == 21:
        print("\n" + "You hit 21!\n")
        print(name,"Wins!\n")
        playAgain()
    elif cTotal == 21:
        print("The computer hit 21!\n")
        print(name,"loses!\n")
        playAgain()
# if user stays and computer total is greater than or equal to 17
    elif hitPass == "stay" and cTotal >= 17:
        if uTotal > cTotal:
            print("\n" + name,"wins!\n")
            playAgain()
        elif uTotal < cTotal:
            print("\n" + name,"loses!\n")
            playAgain()
        elif uTotal == cTotal:
            print("\n" + name,"and the computer tie!\n")
            playAgain()
    else:
        return




#Display game rules
def gameRules():
    print("                               ### Rules ###")
    print("                            ### Instructions ###")
    print("\n1. The goal of the game is to score 21 points or as near as possible\n",
               "without going over; the two players take turns.")
    print("\n2. This game uses a deck of cards starting with aces only as 1 and 6's as the highest card.\n")
    print("\n3. There are four of each in the deck so you can use more strategy to know what will come next.\n")
    print("\n2. A player who totals over 21 is bust and loses the game.")
    print("\n3. The player whose total is nearest 21, after each player has had a turn, wins the game.")
    print("\n4. In the case of an equally high total, the game is tied.")
    print("\n5. The game is over at the end of a round when:")
    print("     - One or both players are bust.")
    print("     - Both players choose to stay.")
    print("\n6. Once a player totals 14 or more, the player will only draw 1 card for the consecutive turns.")
    print("\n7. The house must draw a card until the total is 17 or higher.\n"
          "     At 17 or higher, the house must stay.\n")
    print("\n8. The first player to score 21 wins the game.\n")



#Determine if the user wants to play again with exception handling
def playAgain():
    response = 0
    while response != "y" or response != "yes" or response != "n" or response != "no":
        try:
            response = input("Would you like to play again (y/n)? :").lower()
            if response == "y":
                main()
            elif response == "n":
                print("\nThank you for playing!")
                print("Goodbye!\n")
                sys.exit(1)
        except SystemExit:
            sys.exit(1)
        except TypeError:
            print("Invalid response. Try again.")
            raise
        except ValueError:
            print("Invalid response. Try again.")
            raise
        except:
            print("Invalid response. Try again.")
            raise



#ramdomly choose a card from the deck, remove it from the deck, and return it
def dealCard(cards):
    pickCard = random.choice(cards)
    cards.remove(pickCard)
    return pickCard, cards



#Deals initial cards to the user and computer and displays user and computer totals then returns the total
def startGame(cards, name):
        userCard1, cards = dealCard(cards)
        userCard2, cards = dealCard(cards)
        userTotal = userCard1 + userCard2
        computerCard1, cards = dealCard(cards)
        computerCard2, cards = dealCard(cards)
        computerTotal = computerCard1 + computerCard2
        print("--------------------------------------")
        print("Let's play Blackjack!")
        print("--------------------------------------")
        printPause("")
        print(name + "'s total is:", userTotal)
        printPause("")
        printPause("--------------------------------------")
        printPause("")
        print("The Dealers total is:", computerTotal) 
        printPause("")
        return (userTotal, computerTotal, cards)




def main():
#Display Welcome message
    print("--------------------------------------")
    printPause("Welcome to Blackjack!!!")
    printPause("--------------------------------------")
    printPause("")
    # Declare Variables
    userTotal = 0
    userName = getUserName()
    computerTotal = 0
    userChoice = True

    # Start with the user in the game menu
    choice = gameMenu(userName)
    if choice == 3:
        exit()

    # deckCards is assigned to a list equal to 1 decks of cards up to the 7's 
    deckCards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]

    # Start the game expecting userTotal, computerTotal, and deckCards(with dealt cards removed) returned.
    userTotal, computerTotal, deckCards = startGame(deckCards, userName)

    # determineWinLoss function passing userTotal, computerTotal, userName, and userChoice
    determineWinLose(userTotal, computerTotal, userName, userChoice) 

    # determine if the user wants to hit or stay
    userChoice = hitOrStay()

    # While user input is not equal to stay
    while userChoice == "hit":
    # playerTurn function with userTotal, userChoice and deckCards as parameters
        userTotal, deckCards = playerTurn(userTotal, deckCards, userName)
    # computerTurn function with computerTotal as parameter
        computerTotal, deckCards = computerTurn(computerTotal, deckCards)
    # determineWinLoses function passing userTotal, computerTotal, userName, and userChoice
        determineWinLose(userTotal, computerTotal, userName, userChoice)
        userChoice = hitOrStay()
    # Continue until the computer has more than 17.
    while computerTotal < 17:
        computerTotal, deckCards = computerTurn(computerTotal, deckCards)
        determineWinLose(userTotal, computerTotal, userName, userChoice)
    determineWinLose(userTotal, computerTotal, userName, userChoice)

main()




