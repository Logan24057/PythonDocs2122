#Lump
#Random Dice Generator
#For Dungeons & Dragons and other dice games

#imports the random module
import random

#sets up the variables we will use in this program
diceAmount = 1
diceSides = 6
modifier = 0
programRunning = True
result = 0

#Loop for as long as the program needs to run
while programRunning:
    diceAmount = input("How many dice are you rolling? ")
    print()
    #change diceAmount into an integer
    diceAmount=int(diceAmount)
    #If they type '0' for diceAmount, the loop should quit immediately, use break
    if diceAmount<=0:
        break 
    diceSides = input("How many sides does your dice have? ")
    print()
    #change dice sides to an integer
    diceSides=int(diceSides)
    modifier = input("What should I add to the total result? ")
    print()
    #change modifier to integer
    modifier=int(modifier)
    loops = diceAmount
    #Loops until their are 0 dice left to roll
    while loops > 0 :
        loops -= 1
        result += random.randint(1, diceSides)
    result += modifier
    print('You rolled a total of ' +str(result))
    print()
programmingRunning=False

