word = "abroad"

usedLetters = []

wordBoard = ["_","_","_","_","_","_"]

def showBoard(wordBoard):
    print(wordBoard)

showBoard(wordBoard)
chances = 5

def checkGuess(letter, wordBoard):
    count = 0
    for i in range(0, len(word)):
        if (word[i] == letter):
            wordBoard[i] = letter
            count += 1
    print(wordBoard)
    return count


while(chances):
    newLetter = input("Please guess a letter: ")
    result = checkGuess(newLetter, wordBoard)

    if(result == 0):
        chances -=1
        print(f"There are no {newLetter}'s in the word.")
        print(f"You have {chances} chances left.")
    elif(result == 1):
        print(f"There is one {newLetter} in the word.")
    elif(result > 1):
        print(f"There are {result} {newLetter}'s in the word.")

    if(wordBoard.count("_") == 0):
        print("Congratulations, you have guessed the word!")
        break

if(chances == 0):
    print("Sorry you have run out of chances.")
