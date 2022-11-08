# A Bunch of Card games

# TODO Create Card UI
# TODO Drag Cards
# TODO Shuffle Deck / Interact
# TODO Flip Cards over
# TODO Snap the POS of the card

# TODO Games will be Blackjack, Garbage, Crazy 8's, and Solitaire

# TODO Display anything on a webpage
import json

import deck
import flask
import games.blackjack as blackjack
import games.garbage as garbage
import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/templates/index.html')
def index():
    return render_template('index.html', credits=random.choice(['Sean & Zack', 'Zack & Sean']))


# Blackjack
@app.route('/blackjack/')
def startBlackjack():
    firstWin = blackjack.startOver()    
    if firstWin != '':
        return render_template('blackjack.html', 
                               playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.convertToHTMLString(blackjack.houseHand),
                               winLose=firstWin, 
                               playerTotal=blackjack.getTotal(blackjack.playerHand),
                               houseTotal=blackjack.getTotal(blackjack.houseHand))
    else:
        return render_template('blackjack.html', 
                               playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                               playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/blackjackAddCard/')
def blackjackAddCard():
    blackjack.playerTurn('hit')
    if blackjack.getTotal(blackjack.playerHand) > 21:
        return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                               playerTotal=blackjack.getTotal(blackjack.playerHand), winLose='You Busted.')
    return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                           houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                           playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/blackjackEndPlay/')
def blackjackEndPlay():
    winLose = blackjack.checkWinLose()
    blackjack.gameOver = True
    return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                           houseHand=blackjack.convertToHTMLString(blackjack.houseHand),
                           winLose=winLose, playerTotal=blackjack.getTotal(blackjack.playerHand),
                           houseTotal=blackjack.getTotal(blackjack.houseHand))


# Garbage
@app.route('/garbage/')
def startGarbage():
    if len(garbage.playerHand) == 0:
        garbage.startNewGame()
    return render_template('garbage.html', playerHand=deck.convertToHTMLString(garbage.playerHand))


@app.route('/garbageCardData/<string:cardData>', methods=['POST', 'GET'])
def useCardData(cardData):
    cardData = json.loads(cardData)
    if garbage.playerHand[cardData] == '0':
        garbage.playerHand[cardData] = deck.getNewCard()
    print(garbage.playerHand)
    #return render_template('garbage.html', playerHand=deck.convertToHTMLString(garbage.playerHand))
    return {'playerHand': deck.convertToHTMLString(garbage.playerHand)}


@app.route('/solitaire/')
def startSolitaire():
    return render_template('solitaire.html')


@app.route('/crazy8/')
def startCrazy8():
    return render_template('crazy8.html')


# Misc
@app.route('/return/')
def returnToLanding():
    return flask.redirect('/templates/index.html')


@app.route('/')
def blank():
    return flask.redirect('/templates/index.html')


app.run(host='0.0.0.0', port=5500, debug=True)
