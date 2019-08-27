import random


def isValid(word):

    if word.isdigit():
        print("Please enter a letter")
        return False

    if len(word) > 1:
        print("Please enter one letter at a time!")
        return False

    if len(word) is 0:
        print("Please enter a letter!")
        return False
    return True


def getIndex(letter, word):
    ourIndex = []
    if letter in word:
        for ind in range(len(word)):
            if word[ind] == letter:
                ourIndex.append(ind)
    return ourIndex


class Static:
    word = ""
    wordVList = []
    lives = 0
    totalPoints = 0


def checkIf(letter, word):
    indexes = getIndex(letter, word)

    if len(indexes) is 0:
        print("X" * Static.lives)
        Static.lives += 1

    if len(indexes) is 1:
        Static.wordVList[indexes[0]] = letter

    else:
        for i in indexes:
            Static.wordVList[i] = letter

    indexes.clear()


def uptadeUser():
    strWord = "".join(Static.wordVList)
    print(strWord.capitalize())


def score():
    multiplier = sum([item == " _ "for item in Static.wordVList])

    if len(Static.wordVList) <= 3:
        point = 50
    elif len(Static.wordVList) <= 5:
        point = 100
    elif len(Static.wordVList) <= 7:
        point = 150
    else:
        point = 200

    total = point * multiplier
    return total


def newGame():
    currWord = words[random.randint(0, len(words) - 1)]
    Static.lives = 1
    if Static.word is not currWord:
        Static.wordVList.clear()
        for i in range(len(currWord)):
            Static.wordVList.append(" _ ")
    Static.word = currWord
    return currWord


def prepareWord(word):
    fixedw = word.replace(" ", "").lower()
    return fixedw


with open("words.txt", "r") as f:
    words = f.readlines()

while True:

    print("""1.Start
2.Exit""")
    selection = int(input(">"))

    while selection == 1:

        currWord = newGame().replace("\n", "")

        while True:
            guessed = False
            uptadeUser()
            print("""Enter 1 If You Want To Make a Guess
Don't Have a Guess Yet? Then Enter a Letter
Enter 2 If You Want To End The Round""")

            guess = prepareWord(input(">"))
            try:
                if int(guess) == 1:
                    guessed = True
                    print("Enter Your Guess")
                    guess = prepareWord(input(">"))
                    if guess == currWord:
                        Static.totalPoints += score()
                        print("You Guessed It Right!"
                              f"Score: {Static.totalPoints}")
                        break
                    else:
                        print("You Guessed It Wrong! You Lose a Life")
                        print("X" * Static.lives)
                        Static.lives += 1
                if int(guess) == 2:
                    print(f"Your Total Score {Static.totalPoints}")
                    break
            except ValueError:
                pass

            if not guessed:
                if isValid(guess):
                    if Static.lives is len(currWord)+1:
                        print(f"The Word Was '{currWord.lower().capitalize()}'. You Lose!")
                        break
                    checkIf(letter=guess, word=currWord)
                    if " _ " not in Static.wordVList:
                        print(f"The Word Was '{currWord.lower().capitalize()}'. You Lose a Life. Better Luck Next Time")
                        print("X" * Static.lives)
                        Static.lives += 1

        if selection == 2:
            break


