#Logan Danner
programRunning=True
def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

while programRunning:
    num1=input('What is your first number? ')
    num1=float(num1)
    print()
    num2=input('What is your second number? ')
    num2=float(num2)
    print()
    opChoice=input('What operation would you like to do? ')
    if opChoice=='+':
        print(add(num1,num2))
    elif opChoice=='-':
        print(subtract(num1,num2))
    elif opChoice=='*':
        print(multiply(num1,num2))
    elif opChoice=='/':
        print(divide(num1,num2))
    elif opChoice=='quit':
        programRunning=False
    else:
        print('Invalid Choice')
