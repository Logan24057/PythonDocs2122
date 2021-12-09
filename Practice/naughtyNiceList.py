children=['Bob', 'Susy', 'Mary', 'Joe', 'Bobby', 'Hank', 'Phil', 'Doug', 'Kelly']
naughtyList=[]
niceList=[]

for child in children:
    inputCheck="invalid"
    while inputCheck=="invalid":
        print()
        print('The child is ' +  child)
        print()
        decision=input('Is the child naughty or nice? ')
        print()
        if decision =='na':
            naughtyList.append(child)
            inputCheck='valid'
            print('Children in the Naughty List: ')
            for child in naughtyList:
                print(child)
        elif decision=='ni':
            niceList.append(child)
            inputCheck='valid'
            print('Children in the Nice List: ')
            for child in niceList:
                print(child)
        else:
            print('Your choice was invalid.')
