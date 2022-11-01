import sys
import random

print("================")
print("The Game of War.")
print("by accessdenied.")
print("================")
commence = str(input("Commence Battle? Yes or No.").lower())
while(commence == "yes"):
    values = [1,2,3,4,5,6,7,8,9,10,11]
    cpu = random.choice(values)
    player = random.choice(values)
    
    commence = str(input("Commence Another Battle? Yes or No.").lower()) 