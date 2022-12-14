from itertools import product
from random import shuffle
deck = []


def shuffleDeck():
    global deck
    cardValues = list(range(2, 11)) + list('JQKA')
    deck = [x for x in product([str(cardValue) for cardValue in cardValues], ['Spades', 'Hearts', 'Clubs', 'Diamonds'])]
    shuffle(deck)


def getNewCard(allowShuffle=True):
    if len(deck) == 0:
        if allowShuffle:
            print('Shuffling Deck')
            shuffleDeck()
        else:
            return 'Shuffling is disabled'
    return deck.pop()


def getCardSuitSymbol(card, color='black'):
    if color == 'black':
        if card == '0':
            return '?'
        if card[1] == 'Spades':
            return '♠'
        elif card[1] == 'Hearts':
            return '♥'
        elif card[1] == 'Clubs':
            return '♣'
        elif card[1] == 'Diamonds':
            return '♦'
    elif color == 'white':
        if card[1] == 'Spades':
            return '♤'
        elif card[1] == 'Hearts':
            return '♡'
        elif card[1] == 'Clubs':
            return '♧'
        elif card[1] == 'Diamonds':
            return '♢'


def convertDeckToHTMLString(hand):
    if len(hand) == 0:
        return 'Game Over'
    x = []
    for card in hand:
        string = ''
        string += getCardSuitSymbol(card)
        if card[0] == '1':
            string += 'A'
        else:
            string += card[0]
        x.append(string)
    return x


def convertCardToHTMLString(card):
    if len(card) < 1:
        return '??'
    return getCardSuitSymbol(card) + card[0]
