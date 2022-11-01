import sys
import random

print("================")
print("The Game of War.")
print("by allaccessdenied.")
print("================")
commence = str(input("Commence Battle? Yes or No.").lower())
def cardPicker(comp,play):
    cards = ["",""]

    onecards = ["1H","1D","1S","1C"]
    twocards = ["2H","2D","2S","2C"]
    threecards = ["3H","3D","3S","3C"]
    fourcards = ["4H","4D","4S","4C"]
    fivecards = ["5H","5D","5S","5C"]
    sixcards = ["6H","6D","6S","6C"]
    sevencards = ["7H","7D","7S","7C"]
    eightcards = ["8H","8D","8S","8C"]
    ninecards = ["9H","9D","9S","9C"]
    tenroyalty = ["JH","JD","JS","JC"]
    elevenroyalty = ["QH","QD","QS","QC"]
    twelveroyalty = ["KH","KD","KS","KC"]
    thirteenroyalty = ["AH","AD","AS","AC"] 

    match comp:
        case 1:
            cards[0] = random.choice(onecards)
        case 2:
            cards[0] = random.choice(twocards)
        case 3:
            cards[0] = random.choice(threecards)
        case 4:
            cards[0] = random.choice(fourcards)
        case 5:
            cards[0] = random.choice(fivecards)
        case 6:
            cards[0] = random.choice(sixcards)
        case 7:
            cards[0] = random.choice(sevencards)
        case 8:
            cards[0] = random.choice(eightcards) 
        case 9:
            cards[0] = random.choice(ninecards)
        case 10:
            cards[0] = random.choice(tenroyalty)
        case 11:
            cards[0] = random.choice(elevenroyalty)
        case 12:
            cards[0] = random.choice(twelveroyalty)
        case 13:
            cards[0] = random.choice(thirteenroyalty)
    match play:
        case 1:
            cards[1] = random.choice(onecards)
        case 2:
            cards[1] = random.choice(twocards)
        case 3:
            cards[1] = random.choice(threecards)
        case 4:
            cards[1] = random.choice(fourcards)
        case 5:
            cards[1] = random.choice(fivecards)
        case 6:
            cards[1] = random.choice(sixcards)
        case 7:
            cards[1] = random.choice(sevencards)
        case 8:
            cards[1] = random.choice(eightcards) 
        case 9:
            cards[1] = random.choice(ninecards)
        case 10:
            cards[1] = random.choice(tenroyalty)
        case 11:
            cards[1] = random.choice(elevenroyalty)
        case 12:
            cards[1] = random.choice(twelveroyalty)
        case 13:
            cards[1] = random.choice(thirteenroyalty)
    return cards

while(commence == "yes"):
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
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