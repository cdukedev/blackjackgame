# Marjorie Issue #9- Roll Dice Function

# Import random library to generate random numbers during the dice rolls
import random
dice1RollValue = random.randint(1,6)
dice2RollValue = random.randint(1,6)


# Ask the User if they want to play and roll. 
def main():
    print("Let's Begin Playing Vingt-Et-Un!")
    keepRollingDice = True
    while keepRollingDice == True:
    #Ask player if they would like to play
        player1 = input("Do you want to roll dice? Y/N:").upper()

        if (player1 == "Y" or player1 == "YES"):
            roll2Dice()
        
        else:
            keepRollingDice = False
            
        
def roll2Dice():
    dice1RollValue = random.randint(1,6) #First Dice Roll will randomly land on a number from 1 to 6.
    dice2RollValue = random.randint(1,6) #Second Dice Roll will randomly land on a number from 1 to 6.
    playerOneTotalScore = dice1RollValue + dice2RollValue
    print("You rolled a " + str(dice1RollValue), "and",str(dice2RollValue))
    print("You're total roll score is", playerOneTotalScore)
    playerchoice1 = input("Would you like to (H)IT or (S)TAY ?").upper()
    if (playerchoice1 == "H" or playerchoice1 == "HIT"):
        print("Great!.. Let's Roll the Dice Again!!")
        dice1RollValue = random.randint(1,6) #First Dice Roll will randomly land on a number from 1 to 6.
        dice2RollValue = random.randint(1,6) #Second Dice Roll will randomly land on a number from 1 to 6.
        playerOneTotalScore = dice1RollValue + dice2RollValue
        print("You rolled a " + str(dice1RollValue), "and",str(dice2RollValue))
        print("You're total roll score is", playerOneTotalScore)
        playerchoice1 = input("Would you like to (H)IT or (S)TAY ?").upper()
    elif (playerchoice1 == "S" or playerchoice1 == "STAY"):
        print("Ok. You decided to Stay. It's the Dealer's Turn") 
    



main()
