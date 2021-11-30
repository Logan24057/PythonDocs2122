#Logan
import time

kittensToPunt=input("How many homeless kitten's would you like to punt? ")
#change kittensToPunt into a int
kittensToPunt=int(kittensToPunt)

puntCounter=0

print(puntCounter)
#create a while loop that loops until there are no kittens left to punt
while puntCounter<kittensToPunt:
    print("You successfully punted a kitten!")
    
    time.sleep(1)
    
    #every time a kitten is punted add one to the punt counter
    puntCounter+= 1
    print()
    #print "Kittens left to punt" + kittensToPunt minus puntCounter as a string
    print("Kittens left to punt " + str(kittensToPunt-puntCounter))
    print()
    print(puntCounter)
