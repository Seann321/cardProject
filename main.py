# A Bunch of Card games

# TODO Create Card UI
# TODO Drag Cards
# TODO Shuffle Deck / Interact
# TODO Flip Cards over
# TODO Snap the POS of the card

# TODO Games will be Blackjack, Garbage, Crazy 8's, and Solitaire

# TODO Display anything on a webpage
import deck
import flask
import games.blackjack as blackjack
import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/templates/index.html')
def index():
    return render_template('index.html', credits=random.choice(['Sean & Zack', 'Zack & Sean']))


@app.route('/blackjack/')
def my_link():
    firstWin = blackjack.startOver()
    if firstWin:
        blackjack.gameOver = True
        winLose = blackjack.checkWinLose()
        return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                               winLose=winLose, playerTotal=blackjack.getTotal(blackjack.playerHand),
                               houseTotal=blackjack.getTotal(blackjack.houseHand))
    else:
        return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                               playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/blackjackAddCard/')
def blackjackAddCard():
    blackjack.playerTurn('hit')
    return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                           houseHand=blackjack.convertToHTMLString(blackjack.houseHand, True),
                           playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/blackjackEndPlay/')
def blackjackEndPlay():
    winLose = blackjack.checkWinLose()
    blackjack.gameOver = True
    return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand), houseHand=blackjack.convertToHTMLString(blackjack.houseHand),
                           winLose=winLose, playerTotal=blackjack.getTotal(blackjack.playerHand),
                           houseTotal=blackjack.getTotal(blackjack.houseHand))


@app.route('/')
def blank():
    return flask.redirect('/templates/index.html')


app.run(host='0.0.0.0', port=5500, debug=True)
