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
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/templates/index.html')
def index():
    card = deck.getNewCard()
    return render_template('index.html', cardValue=f'{card[0]}', cardSuit=f'{deck.getCardSuitSymbol(card, "white")}')


@app.route('/blackjack/')
def my_link():
    firstWin = blackjack.startOver()
    if firstWin:
        blackjack.gameOver = True
        winLose = blackjack.checkWinLose()
        return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.houseHand,
                               winLose=winLose, playerTotal=blackjack.getTotal(blackjack.playerHand))
    else:
        return render_template('blackjack.html', playerHand=blackjack.convertToHTMLString(blackjack.playerHand),
                               houseHand=blackjack.houseHand[0],
                               playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/blackjackAddCard/')
def blackjackAddCard():
    blackjack.playerTurn('hit')
    return render_template('blackjack.html', playerHand=blackjack.playerHand, houseHand=blackjack.houseHand[0],
                           playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/blackjackEndPlay/')
def blackjackEndPlay():
    winLose = blackjack.checkWinLose()
    blackjack.gameOver = True
    return render_template('blackjack.html', playerHand=blackjack.playerHand, houseHand=blackjack.houseHand,
                           winLose=winLose, playerTotal=blackjack.getTotal(blackjack.playerHand))


@app.route('/')
def blank():
    return flask.redirect('/templates/index.html')


app.run(host='0.0.0.0', port=5500)
