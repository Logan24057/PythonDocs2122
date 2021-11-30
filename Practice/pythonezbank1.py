#Logan EZBank 1

#imports our custom module
import basics

#create a new app and user object from the basics module
app=basics.newProgram()
user=basics.newUser()

#store the users bank balance as a property of the app
app.balance=1000

#loop while the app.running is true
while app.running :
    print(app.balance)
    #ask the user to select an option
    user.choice=input('1:Deposit,2:Withdraw,or 3:Quit ')
    #input always returns a string, so compare to a string
    if user.choice=='1' :
        #ask how much they want to deposit
        user.deposit=input('How much would you like to deposit? ')
        #check to make sure the input was a number that can be converted
       

    elif user.choice=='2' :
        #Ask for a withdraw amount
        user.withdraw=input('How much would you like to withdraw? ')
        #check to see if input was a number
        user.withdraw=int(user.withdraw)
        #subtract from balance if they have enough to withdraw
        if user.withdraw > app.balance:
            print('You do not have enough money.')
        else:
            app.balance-=user.withdraw
    elif user.choice=='3':
        #make running False so the loop does not continue
        app.running=False

    else :
        print('Your choice was invalid')
        


