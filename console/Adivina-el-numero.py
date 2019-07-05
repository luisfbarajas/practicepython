import random

Trys = 0
# Say hi!
print("Hello! What's your name?")
myName = input()

# Get a random number
number = random.randint(1,20)

print('Well, '+myName+', i\'m thinking in a number betwen 1 adn 20.')

while Trys < 6:
    print('Go ahead try it!')
    estimate = input()
    estimate = int(estimate)

    Trys =  Trys + 1

    if estimate < number:
        print('Your estimate too low.') #Message low number
    if estimate > number:
        print('Your estimate is too high.')# Message high number
    if estimate == number:
        break
if estimate == number:
    Trys = str(Trys)
    print('Good job!! '+myName+' you guessed mi number in '+Trys+' trys! My number was '+ str(number)) #Win message

if estimate != number:
    number = str(number)
    print('Well nice try. But you lose...LOSER!!!!!!!!') #Lose message
    
    