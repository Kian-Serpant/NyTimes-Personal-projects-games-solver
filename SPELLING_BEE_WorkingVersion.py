myFile = open("words.txt")
preletters = ["P","I","A","R","O","N"]
forcedletter = "D"
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