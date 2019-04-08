import json
import datetime
import random
from database import readFile
from database import writeFile
def playGame(nuo, iki):
    skaicius = random.randint(nuo, iki)
    turn = 0
    paskutinis_spejimas = 0
    while skaicius != paskutinis_spejimas:
        print("Musu skaicius " + str(skaicius))
        turn = turn + 1
        currentTurn = str(turn)
        guess = int(input(currentTurn + " guess. Guess the number:"))
        if checkNumber(guess, skaicius):
            print("Congratulations")
            break
        else:
            print("Try again")
        print(giveHint(skaicius, guess))
        paskutinis_spejimas = guess
    addScore(turn)
    print("Zaidimas baigtas, pabaiga cia")
    print("Atspeti tau uztruko " + str(turn) + " spejimus")
def checkNumber(numberProvided, numberToGuess):
    if numberProvided == numberToGuess:
        return True
    else:
        return False
def printHighscores():
    scores = getScores()
    print("Sveiki! Top rezultatas yra:")
    place = 1
    for score in scores[:3]:
        print(str(place) + " vieta: " + str(score["attempts"]) + "(" + str(score["date"]) + ")")
        place += 1
    print("-----")
def giveHint(number_to_guess, number_guessed):
    if number_to_guess > number_guessed:
        return "Daugiau"
    return "Maziau"
def getScores():
    highscore_data = readFile("highscore.txt")
    scores = json.loads(highscore_data)
    return scores
def addScore(score):
    score_date = str(datetime.datetime.now())
    score_record = {
        "date": score_date,
        "attempts": score
    }
    scores = getScores() # Gaunam esamus taskus
    scores.append(score_record) # Pridedam naujus taskus
    data = json.dumps(scores) # Isverciam list'a atgal i JSON
    writeFile("highscore.txt", data) # Irasom i rezultatu faila nauja list'a
