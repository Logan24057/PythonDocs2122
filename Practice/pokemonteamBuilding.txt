#Logan
#import gen1 pokedex
import gen1

#create a empty list for your pokemon team
pokemonTeam=[]

#set program running to true
programRunning=True

#create a while loop
while programRunning:
    for pokemon in pokemonTeam:
        print(pokemon)

    print()
    # ask the user if they would like to add, remove, or quit
    playerChoice=input('Add, Remove, or Quit. ')
    print()
    #make an if statement for the add choice
    if playerChoice.lower()=='add':
        #if the pokemon team is 6 pokemon or larger tell the user there is not enough room
        if len(pokemonTeam) >= 6 :
            print('There isnt enough room to add a pokemon to the team.')
            print()
        else:
            #if there is enough room ask the user what pokedex number they want to add
            playerChoice=input('What is the pokedex number of the pokemon you want to add? ')
            print()
            #change the users choice to an integer
            playerChoice=int(playerChoice)
            #if the users choice is greater than 150 or less than 1 tell that this is only the first gen pokedex(only 150 pokemon)
            if playerChoice >150 or playerChoice <1 :
                print('First Generation Pokedex only(First 150).')
            else:
                #add the users pokedex choice to their pokemon team
                pokemonTeam.append(gen1.pokedex[ playerChoice -1])

    # for if the user chose remove
    elif playerChoice.lower()=='remove':
        #create a counter and set to zero
        counter=0
        #for each pokemon in the pokemon team add 1 to the counter
        for pokemon in pokemonTeam:
            counter = counter+1
            #print the counter and the pokemon
            print(counter, pokemonTeam[counter -1])
            #ask the user which number they want to remove
        playerChoice=input('Which number do you want to remove? ')
        playerChoice=int(playerChoice)
        #if the users choice is greater or less than the length of their team tell them its invalid
        if playerChoice-1 > len(pokemonTeam) or len(pokemonTeam) <0:
            print('Invalid Number.')
        else:
            #remove the users chosen number from the pokemon team
            pokemonTeam.remove(pokemonTeam[playerChoice-1])
    #if users choice was quit stop running the program
    elif playerChoice.lower()=='quit':
        programRunning=False

    else:
        print('Your choice was invalid.')
