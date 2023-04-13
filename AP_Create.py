import colorama
from colorama import Fore
from colorama import Style
import random
import sys
print("\033c", end='')


def numberChecker(word):
    for i in range(9):
        if str(i) in word:
            return False
    return True

def letterToLetter(Letter, List2):
    if (Letter in List2):
        return True
    else:
        return False

def indexChecker(Letter, List2, count):
    for i in range(count, len(List2)):
        if (Letter == List2[i]):
            return i
            


colorama.init()
WordList = []
letters = []
guessList = []
file = open('valid-wordle-words.txt', 'r')
#print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
#print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
#print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
#print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)




#Start of the game and Introduction. 
for each in file:
    WordList.append(each)
print("Words are done loading! You are ready to play.\n")
print("Welcome to Wordle!")

start = input("Please press \"Enter\" to play.")
while(start != ""):
    start = input("Please press \"Enter\" to play.")




#Step1: getting the word.
randomNum = random.randint(0, len(WordList))
letters = list(WordList[randomNum]) 
letters.remove("\n") 
#answer key
print(letters)





#Step2: Letting the person guess:
for i in range(6):
    guesses = ""
    while (len(guesses) != 5 or not numberChecker(guesses)):
        guesses = input("Guess a 5 letter word. " + str(6 - i) + " attempts remaining:\n")
        guessList = list(guesses)
    
    if (guessList == letters):
        print("\nYou Win Congrats!")
        sys.exit() 
    else:
        count = 0
        for i in guessList:
            if (letterToLetter(i, letters)):
                if (count == indexChecker(i, letters, count)):
                    print(Fore.GREEN + i + Style.RESET_ALL, end = "")
                else:
                    print(Fore.YELLOW + i + Style.RESET_ALL, end = "")
            else:
                print(i, end = "")

            count += 1
        print()

print("You lose. The word was: " + WordList[randomNum])
            




#five letter with 6 att
#yellow background means right letter wrong place
#gray means wrong letter
#green means right letter right place

# Step 1: We get random word. 
# Step 2: The random word will be split into a list.
# Step 3: User has 6 tries to guess the word.
# Step 4: Each guess is put into list to compare and color code the thingy.
# Step 5: Then color code word. 
# Step 6: If word is guessed correctly, they win, else they lose bozo.






















