#Logan

#ask the user how much they enjoy computer programming on a scale of 1-10
userScale=input("On a scale of 1-10, how much do you enjoy Computer Programming Class? ")

#convert the users answer to an integer
userScale=int(userScale)

#if the users answer equals 10 or 9 have is say "I think programming is great too"
if userScale== 10 or userScale== 9:
    print("I think programming is great, too.")
    print()
#if the users answer equals 8 or 7 say "Im glad you enjoy it"
elif userScale == 8 or userScale==  7:
    print("Im glad you enjoy it.")
    print()
#if the users answer equals 6 or 5 say "Well programming isnt for everyone"
elif userScale== 6 or userScale== 5:
     print("Well programming isn't for everyone.")
     print()
#otherwise say "That's ok. I'm sure you will make a good burger-flipper one day."
else:
    print("That's ok. I'm sure you will make a good burger-flipper one day.")
