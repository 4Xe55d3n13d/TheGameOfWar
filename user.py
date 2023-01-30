import sys
import random
from random import choice

print("================")
print("The Game of War.")
print("by allaccessdenied.")
print("================")
commence = input("Commence Battle? Yes or No.").lower()

def cardPicker(comp,play):
    vals = list(range(2, 11)) + list('JQKA')
    deck = [[str(val) + suit for suit in 'HDSC'] for val in vals]
    return [choice(deck[comp]),choice(deck[play])]

while(commence == "yes"):
    values = list(range(2,12))
    
    cpu = random.choice(values)
    player = random.choice(values)
    cardsDrawn = cardPicker(cpu,player)

    print("You drew a " + cardsDrawn[1])
    print("CPU drew a " + cardsDrawn[0])

    if(cpu > player):
        print("CPU wins.")
    elif(cpu < player):
        print("Player wins.")
    else:
        print("Draw.")

    commence = str(input("Commence Another Battle? Yes or No. ").lower()) 