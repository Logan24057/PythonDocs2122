#import basics module to use its code
import basics

#make new app object from the basics module
app=basics.newProgram()

#use method that belongs to our new application object
app.print('yo momma')

#print property of new application object
app.print(app.debugging)

#this line wont print if app.debugging is False
app.debug("Hello")
#we will enable debugging for application
app.debugging=True
app.debug('Now it Works!!')

#import default python modeule
import random

#use a method from the random module
randomNumber=random.randint(1, 10)
app.print(randomNumber)

