myFile = open("WordleFile.txt")

# code to get a list of the letters that were wrong from the user
def getWrongLetters():
    x = input("What letters are NOT in the word:")
    newWrongLetters = []
    for letter in x:
        if (ord(letter.upper()) >= 65 and ord(letter.upper()) <= 90) and (letter.upper() not in newWrongLetters):
            newWrongLetters.append(letter.upper())

    return newWrongLetters

# code to get which yellow letters are known for each position
def getYellowLetters():
    currentYellows = [[],[],[],[],[]]
    allYellows = []
    posLoc = 1
    yellowsKnown = input("Do you have any yellow letters(yes/no)? ")
    if (yellowsKnown.upper() == "Y") or (yellowsKnown.upper() == "YES"):
        for position in currentYellows:
            y = input(f"What yellow letters are in position {posLoc} (blank if none known): ")
            for letter in y:
                if (ord(letter.upper()) >= 65) and (ord(letter.upper()) <= 90):
                    position.append(letter.upper())
                    if letter not in allYellows:
                        allYellows.append(letter.upper())
            posLoc += 1
    return currentYellows, allYellows

# function for getting which letters are correct and which spots they are in
def getCorrectLetters():
    correctLetters = [".", ".", ".", ".", "."]
    userHaveCorrectLetters = input("Do you know the correct positions for any letters(yes/no or y/n)? ")
    if (userHaveCorrectLetters.upper() == "YES") or (userHaveCorrectLetters.upper() == "Y"):
        for letterCount in range(1,6):
            userLetter = input(f"What is the letter in position {letterCount} (leave blank if unknown): ")
            if userLetter != "":
                if (ord(userLetter.upper()) >= 65) and (ord(userLetter.upper()) <= 90):
                    correctLetters[letterCount - 1] = userLetter.upper()
            letterCount+= 1

    return correctLetters

# Function that does all the logic of searching the text file for words that fit the criteria.
def getWords3():
    wrongLetters = getWrongLetters()
    yellowLetters, allPossYellows = getYellowLetters()
    correctLetters = getCorrectLetters()

    possibleWords = []
    for words in myFile:
        wordfine = True
        for letter in wrongLetters:
            if (letter in correctLetters):
                pass
            elif not (letter in words.strip().upper()):
                if len(yellowLetters) != 0:
                    for correctLetter in allPossYellows:
                        if not (correctLetter in words.strip().upper()):
                            wordfine = False
            else:
                wordfine = False
        if wordfine:
            for letter in words.strip().upper():
                if ((ord(letter) < 65) or (ord(letter) > 90)):
                    wordfine = False
            if wordfine:
                possibleWords.append(words.strip())

    # checking for correct letters below here:
    possWords = []

    for word in possibleWords:
        wordFine = True
        for numb in range(0, 5):
            if (correctLetters[numb] != "."):
                if correctLetters[numb] != word[numb].upper():
                    wordFine = False
            if word[numb].upper() in yellowLetters[numb]:
                wordFine = False
        if wordFine:
            possWords.append(word)

    return possWords

possibleWords = getWords3()
print(possibleWords)
print("Just to let you know, some of the words here are not included in the official wordle dictionary,"
      "this was not a dictionary I was able to find unfortunately")
