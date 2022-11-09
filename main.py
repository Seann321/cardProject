"""
A bunch of card games. Including Blackjack, Garbage, Solitaire, and Crazy 8's
Created by Sean (Backend), and Zack (Frontend).
Might put multiplayer in at some point. Currently just going to get the single-player working.
Do note that some games use different methods for networking, as I am learning as I go.
 - Sean
"""

import json
import deck
import flask
import games.blackjack as blackjack
import games.garbage as garbage
import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/templates/index.html')
def index():
    return render_template('index.html', credits=random.choice(['Sean & Zack', 'Zack & Sean']))


# Blackjack
def blackjackJSONData(houseCard=False, winLose=''):
    if houseCard:
        return {'playerHand': blackjack.convertToHTMLString(blackjack.playerHand),
                'houseHand': blackjack.convertToHTMLString(blackjack.houseHand, houseCard),
                'winLose': winLose,
                'playerTotal': blackjack.getTotal(blackjack.playerHand)}
    return {'playerHand': blackjack.convertToHTMLString(blackjack.playerHand),
            'houseHand': blackjack.convertToHTMLString(blackjack.houseHand),
            'winLose': winLose,
            'playerTotal': blackjack.getTotal(blackjack.playerHand),
            'houseTotal': blackjack.getTotal(blackjack.houseHand)}


@app.route('/blackjack/')
def startBlackjack():
    firstWin = blackjack.startOver()
    if firstWin is not None:
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
        return render_template('blackjack.html',
                               playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                               playerTotal=blackjack.getTotal(blackjack.playerHand), winLose='You Busted.')
    return render_template('blackjack.html',
                           playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
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
def garbageJSONData(invalidMove=False, gameOver=False):
    return {'playerHand': deck.convertDeckToHTMLString(garbage.playerHand), 'invalidMove': invalidMove,
            'currentCard': deck.convertCardToHTMLString(garbage.cardSelected), 'gameOver': gameOver,
            'discardedCard': deck.convertCardToHTMLString(garbage.discardedCard),
            'AIHand': deck.convertDeckToHTMLString(garbage.AIHand)}


@app.route('/garbage/')
def startGarbage():
    return render_template('garbage.html')


@app.route('/initGarbage/')
def initGarbage():
    return garbageJSONData()


@app.route('/garbageReset/')
def resetGarbage():
    garbage.restart()
    return flask.redirect('/garbage')


@app.route('/garbageCardData/<string:cardData>')
def garbageCardData(cardData):
    cardData = json.loads(cardData)
    if len(garbage.cardSelected) == 0:
        return garbageJSONData(invalidMove=True)
    else:
        if garbage.switchCardsValid(cardData):
            # If spot is unknown
            if garbage.playerHand[cardData] == '0':
                garbage.playerHand[cardData] = garbage.cardSelected
                garbage.choiceNewCard(deck.getNewCard())
            # If card already in spot
            else:
                temp = garbage.playerHand[cardData]
                garbage.playerHand[cardData] = garbage.cardSelected
                garbage.cardSelected = temp
            if garbage.checkForWin():
                if garbage.playerCardCount == 0:
                    # Game Over
                    return garbageJSONData(gameOver=True)
                else:
                    garbage.playerCardCount -= 1
                    garbage.restart(garbage.playerCardCount, garbage.AICardCount)
            return garbageJSONData()
        else:
            return garbageJSONData(invalidMove=True)


@app.route('/garbageDeckPull/')
def garbageDeckPull():
    garbage.cardSelected = deck.getNewCard()
    return garbageJSONData(invalidMove=False)


@app.route('/garbageDiscardCard/')
def garbageDiscardCard():
    garbage.discardCard()
    return garbageJSONData(invalidMove=False)


@app.route('/garbagePullFromDiscard/')
def garbagePullFromDiscard():
    garbage.pullFromDiscard()
    return garbageJSONData(invalidMove=False)


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
