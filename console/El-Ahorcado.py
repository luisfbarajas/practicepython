# imports
import random

# constance for image of the game
IMAGENES_AHORCADO = ['''
  
     +---+
     |   |
         |
         |
         |
         |

   =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
# string whit random words
words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

# This function return a secret word of listwprds
def getrandomWord(listOfWords):
    indexOfWords = random.randint(0,len(listOfWords)-1)
    return listOfWords[indexOfWords]

# show results to player 
def showTable(IMAGENES_AHORCADO, lettersWrong, lettersRight, secretWord):
    print(IMAGENES_AHORCADO[len(lettersWrong)])
    print()

    print('letters wrong: ', end =' ')
    # for loop to print letters wrong
    for letter in lettersWrong:
        print(letter, end = ' ')
    print()

    whiteSpaces = '_' * len(secretWord)
    for i in range(len(secretWord)): #complete the empt spaces with guessed letters
        if secretWord[i] in lettersRight:
            whiteSpaces = whiteSpaces[:i] + secretWord[i] + whiteSpaces[i+1:]
        

def getTry(testLetter):
    while True:
        print('guess the letter')
        trys = input()
        trys = trys.lower()
        if len(trys) != 1:
            print('Please, introduce another letter.')
        elif trys in testLetter:
            print('You already prube that letter man, comon! choose another.')
        elif trys not in 'abcdefghijklmnñopqrstuvwxyz':
            print('letters! not numbers please.')
        else:
            return trys
# This function return true if the player wanna try again and false if dont want to try
def playAgain():
    print('Wanna play again body? (Yes/No)')
    return input().lower().startswith('s')

print('A H O R C A D O')
lettersright = ''
lettersWrong = ''
secretWord = getrandomWord(words)
endGame = False


while True:
    showTable(IMAGENES_AHORCADO, lettersWrong,lettersright, secretWord)

    # let write a letter
    trys = getTry(lettersWrong + lettersright)

    if trys in secretWord:
        lettersright = lettersright + trys

        #check if the player win
        findAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in lettersright:
                findAllLetters = False
                break
        if findAllLetters:
            print('Yeah man! you got the right word '+ secretWord + ' you win dude!!')
    else:
        lettersWrong = lettersWrong + trys

        #check if the player don't have try's and lose
        if len(lettersWrong) == len(IMAGENES_AHORCADO)-1:
            showTable(IMAGENES_AHORCADO,lettersWrong,lettersright,secretWord)
            print('Well nice try but you lose, the secret word was: '+ secretWord)
            endGame = True
    #ask for play again
    if endGame:
        if playAgain():
            lettersWrong=''
            lettersright=''
            endGame = False
            secretWord = getrandomWord(words)
        else:
            break
            
