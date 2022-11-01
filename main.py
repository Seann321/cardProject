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
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    card = deck.getNewCard()
    return render_template('index.html', cardValue=f'{card[0]}', cardSuit=f'{deck.getCardSuitSymbol(card, "white")}')


@app.route('/')
def blank():
    return flask.redirect('/index')


app.run(host='0.0.0.0', port=5500)
