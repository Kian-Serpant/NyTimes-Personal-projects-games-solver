myFile = open("WordleFile.txt")
## code created to get wrong letters etc...
def getWrongLetters():
    x = input("What letters are NOT in the word:")
    newWrongLetters = []
    for letter in x:
        if (ord(letter.upper()) >= 65 and ord(letter.upper()) <= 90) and (letter.upper() not in newWrongLetters):
            newWrongLetters.append(letter.upper())

    return newWrongLetters

# code for checking all words(only input from user is the wrong letters)
def getWords():
    oldwrongLetters = ["A","D","O","I", "M", "P", "C","G","E","Y"]
    wrongLetters = getWrongLetters()

    yellowLetters = ["U", "L"]
    correctLetters = [".", "L", "U", ".", "."]

    possibleWords = []

    for words in myFile:
        wordfine = True
        for letter in wrongLetters:
            if not (letter in words.strip().upper()):
                if len(yellowLetters) != 0:
                    for correctLetter in yellowLetters:
                        if not (correctLetter in words.strip().upper()):
                            wordfine = False
            else:
                wordfine = False
        if wordfine:
            for letter in words.strip().lower():
                if ((ord(letter) < 97) or (ord(letter) > 122)):
                    wordfine = False
            if wordfine:
                possibleWords.append(words.strip())

    ### checking for correct letters:
    possWords = []
    for word in possibleWords:
        wordFine = True
        for numb in range(0,5):
            if (correctLetters[numb] != "."):
                if correctLetters[numb] != word[numb].upper():
                    wordFine = False
        if wordFine:
            possWords.append(word)

    return possWords

### code for yellow letters in each position, and making sure not there
def getYellowLetters():
    currentYellows = [[],[],[],[],[]]
    allYellows = []
    posLoc = 1
    for position in currentYellows:
        y = input(f"What yellow letters are in position {posLoc} (blank if none known): ")
        for letter in y:
            if (ord(letter.upper()) >= 65) and (ord(letter.upper()) <= 90):
                position.append(letter.upper())
                if letter not in allYellows:
                    allYellows.append(letter.upper())
        posLoc += 1
    return currentYellows, allYellows



# code for checking with yellow letters(as inout from user)
def getWords2():
    wrongLetters = getWrongLetters()
    yellowLetters, allPossYellows = getYellowLetters()
    correctLetters = [".", "U", "D", ".", "."]

    possibleWords = []
    wrongWords = []
    for words in myFile:
        wordfine = True
        for letter in wrongLetters:
            if not (letter in words.strip().upper()):
                if len(yellowLetters) != 0:
                    for correctLetter in allPossYellows:
                        if not (correctLetter in words.strip().upper()):
                            wordfine = False
            else:
                wordfine = False
        if wordfine:
            for letter in words.strip().lower():
                if ((ord(letter) < 97) or (ord(letter) > 122)):
                    wordfine = False
            if wordfine:
                possibleWords.append(words.strip())

    ### checking for correct letters:
    possWords = []

    for word in possibleWords:
        wordFine = True
        for numb in range(0, 5):
            if (correctLetters[numb] != "."):
                if correctLetters[numb] != word[numb].upper():
                    wordFine = False
            if word[numb].upper() in yellowLetters[numb]:
                wrongWords.append(word)
                wordFine = False
        if wordFine:
            possWords.append(word)

    return possWords

# abcd = getWords2()

# print(abcd)
# print(len(abcd))

# version for checking with yellow letters(as input from user), and with correct letters input by user
def getWords3():
    wrongLetters = getWrongLetters()
    yellowLetters, allPossYellows = getYellowLetters()
    correctLetters = getCorrectLetters()

    possibleWords = []
    wrongWords = []
    for words in myFile:
        wordfine = True
        for letter in wrongLetters:
            if not (letter in words.strip().upper()):
                if len(yellowLetters) != 0:
                    for correctLetter in allPossYellows:
                        if not (correctLetter in words.strip().upper()):
                            wordfine = False
            else:
                wordfine = False
        if wordfine:
            for letter in words.strip().lower():
                if ((ord(letter) < 97) or (ord(letter) > 122)):
                    wordfine = False
            if wordfine:
                possibleWords.append(words.strip())

    ### checking for correct letters:
    possWords = []

    for word in possibleWords:
        wordFine = True
        for numb in range(0, 5):
            if (correctLetters[numb] != "."):
                if correctLetters[numb] != word[numb].upper():
                    wordFine = False
            if word[numb].upper() in yellowLetters[numb]:
                wrongWords.append(word)
                wordFine = False
        if wordFine:
            possWords.append(word)

    return possWords

# function created to get which letters are correct and where they are:
def getCorrectLetters():
    correctLetters = [".", ".", ".", ".", "."]
    userHaveCorrectLetters = input("Do you know the correct positions for any letters(yes/no or y/n)? ")
    if (userHaveCorrectLetters.lower() == "yes") or (userHaveCorrectLetters.lower() == "y"):
        for letterCount in range(1,6):
            userLetter = input(f"What is the letter in position {letterCount} (leave blank if unknown): ")
            if userLetter != "":
                if (ord(userLetter.upper()) >= 65) and (ord(userLetter.upper()) <= 90):
                    correctLetters[letterCount - 1] = userLetter.upper()
            letterCount+= 1

    return correctLetters


# testFinder = getWords3()
# print(testFinder)

z = getWrongLetters()
print(z)