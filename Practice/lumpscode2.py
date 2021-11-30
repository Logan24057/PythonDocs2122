'''
hello im lump how are you i am a hanzo main.
im learning computer programming but my
doctor says i have a mediccal condtion called
"dumm" this program makes you guess a number
and u get so many guesses. i forget how to
program tho becuse of my conditon. if you
help me i will give you 19 vbucks.
'''
#import random module
import random
userGuess=0
target=0
guesses=3

#Loop until you there are no guesses left
while guesses > 0:
    # sets the target to equal a random number between 1 and 10
    target = random.randint(0, 10)
    #prints out you amount of guesses
    print('You have ' +str(guesses)+ ' guesses left.')
    print()
    #
    userGuess=input("Guess a number. ")
    print()
    #change userGuess into an integer
    userGuess=int(userGuess)
    
    #if the users guess is greater than the target have it tell you that your guess was to high
    if userGuess > target:
        print("You guessed too high.")
        print()
        #subract 1 from your total amount of guesses
        guesses -= 1
        #if the users guess is less than the target have it tell you that your guess was to low
    elif userGuess < target:
        print("You guessed too low.")
        print()
        #subract 1 from your total amount of guesses
        guesses -= 1
        #if the users guess equals the target have it say that you guessed correctly
    elif userGuess == target :
        print("You guessed correctly!")
else :
    #if the guesses equal 0 it says you lost
    guesses == 0
    print('You have lost.')
        
