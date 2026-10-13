yellowletter = "E"
otherletters = ["M","P","H","T","A","Y"]

possibleCombinations = []
amountLoopsLeft = 10

### section for trying to create combos not forcing a specific letter

def createCombos(loopsLeft, currentCombos, otherLetters, currentWord):
    if loopsLeft == 0:
        return currentCombos
    for letter in otherLetters:
        newWord = currentWord + letter
        currentCombos.append(newWord)
        createCombos(loopsLeft - 1, currentCombos, otherLetters, newWord)
    return currentCombos

# preletters = ["a","b","c"]
# y = createCombos(4,[],preletters, "")
# print(y)

### section forcing one letter to be in it
def createCombos2(loopsLeft, currentCombos, otherLetters, currentWord, forcedLetter):
    if loopsLeft == 0:
        return currentCombos
    for letter in otherLetters:
        newWord = currentWord + letter
        if forcedLetter in newWord:
            currentCombos.append(newWord)
        createCombos2(loopsLeft - 1, currentCombos, otherLetters, newWord, forcedLetter)
    return currentCombos

# preletters = ["a","b","c"]
# forcedletter = "D"
# preletters.append(forcedletter)
# z = createCombos2(4,[],preletters, "", forcedletter)
# print(z)

### section for checking if it's in a dictionary
import enchant
import time
mydicti = enchant.Dict("en_US")
def createCombos3(loopsLeft, currentCombos, otherLetters, currentWord, forcedLetter):
    if loopsLeft == 0:
        return currentCombos
    for letter in otherLetters:
        newWord = currentWord + letter
        if forcedLetter in newWord:
            currentCombos.append(newWord)
        createCombos3(loopsLeft - 1, currentCombos, otherLetters, newWord, forcedLetter)
    return currentCombos

preletters = ["M","P","H","T","A","Y"]
forcedletter = "E"
preletters.append(forcedletter)
# x = createCombos3(8,[],preletters, "", forcedletter)
# print("done creating combos")
# print(len(x), "times need to check dictionary")
# time.sleep(3)
# validWords = []
# queryCount = 0
# for word in x:
#     if mydicti.check(word):
#         validWords.append(word)
#     queryCount += 1
#     print(queryCount)
# print(validWords)


### other method instead iterating through the dictionary
preletters = ["M","P","H","T","A","Y"]
forcedletter = "E"
preletters.append(forcedletter)


myFile = open("words.txt")
def check_word_composition_1(word, preletters_set):
    """Returns True if all characters in 'word' are found in 'preletters_set'."""
    # The 'all()' function checks if every item in the generator is True
    return all(char in preletters_set for char in word)

# correctWords = []
# prelettersSet = set(preletters)
# for word in myFile:
#     if forcedletter in word.strip():
#         if check_word_composition_1(word.strip(), prelettersSet):
#             correctWords.append(word.strip())

# print(correctWords)


### more brute force way - FINAL THING
preletters = ["M","P","H","T","A","Y"]
forcedletter = "E"
preletters.append(forcedletter)

def checkLetterInIt(word, letters):
    for letter in word:
        if not (letter.upper() in letters):
            # print(letter, "not in letters")
            return False
    return True

correctWords = []

for word in myFile:
    if forcedletter in (word.strip()).upper():
        if checkLetterInIt(word.strip(), preletters):
            correctWords.append(word.strip())

print(correctWords)
correctWords.sort(key=len)
print(correctWords)