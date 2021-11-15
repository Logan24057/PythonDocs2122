#Logan Danner
#pratice using expressions and conditional statements

#an expression is a problem that must be solved
#5+5 is an "arithmetic" expression
x=5+5

#functions/methods must be resolved as expressions as well
answer=input('What is your name?')

#comparison expressions resolve as True/False
print(7>7)
print(7>=7)
print(x==10)
print(x>10 or x<10)

#a conditional statement runs if its condition is True/ not False
if answer =='Bob':
    print('Hello, Bob! Welcome back!')
    print('This line also prints if your name is Bob')
elif answer == "Vadim":
    print("Im here about your cars extended warranty!")
elif answer=="Doom Slayer":
    print('RIP AND TEAR!!!')
else:
    print("Sorry, I dont talk to Losers")
print('This line isnt inside of the if statement, and prints regards.')

#^ If checks a condition
#^ Elif check a condition if the previous conditions were not true
#^ You can have as many elif's as you want
#^ Else runs if no prior conditions were true

age=input('How old are You?')
age=int(age)
if age>=10:
    print('Here is your license')
elif age==9:
    print('You have one more year to go.')
else :
    print('Ha Too Bad')
