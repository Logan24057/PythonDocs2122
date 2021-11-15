#Logan Danner
#Assignment Examples

#you can assign values to variables by using an equal sign (right side goes into left side)
x=5
# when python reads a variabe name it replaces it with the variables stored value
y=x+5
# there are 4 different primitive datatypes
# integers: any whole number positive or negative
age=16
#float:any number with a decimal, positive or negative
grade=98.6
#String: a string of human-readable characters numbers in a string are not numbers they are letters
name = "Logan"
favoriteNumber="13"
#Boolean: True or False
# true is any value that is not false or empty
isSmart=True

# you can output to the console by using print()
print(age)
print(grade)
print(name)
print(favoriteNumber)
print(isSmart)
#you can concatinate similia values together
print("My name is " + name)
# you can use functions to convert datatypes
print("and my age is " + str(age))
#dont forget! if you want to convert a value permantly you must assign the converted valuable to a variable
age= str(age)
#you can convert back and forth with int(),str(),bool(), and float()
print(int(age))
print(float(age))
print(bool(age))
