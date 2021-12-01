#Logan Danner

programRunning = True

itemList=[]

while programRunning:
    userInput = input('Add,Remove, or Quit. ')
    print()
    if userInput.lower()== 'add':
        userInput=input('What do you want to add? ')
        print()
        itemList.append(userInput)
    elif userInput.lower()== 'remove':
        userInput=input('What do you want to remove? ')
        if userInput in itemList :
            itemList.remove(userInput)
            print()
        else:
            print('Item is not in the list.')
    elif userInput.lower()== 'quit':
        programRunning=False
    else:
        print('Your choice is invalid.')


    print()
    for item in itemList:
        print(item)
        print()
