#Logan

#import the random module
import random

#ask user a yes or no question
userquestion=input("Are you an idiot?")

#generate number between 1 and 4
randNumb=random.randint(1, 4)

# if random number is equal to 1 say yes
if randNumb == 1:
    print("yes")
#if random number is equal to 2 say maybe
elif randNumb== 2:
    print("Maybe")
#if random number is equal to 3 say no
elif randNumb== 3:
    print("No")
#if random number equals 4 say "Why would you even ask that? What is wrong with you? Do you need a therapist? Shame."
elif randNumb== 4:
    print("Why would you even ask that? What is wrong with you? Do you need a therapist? Shame.")
