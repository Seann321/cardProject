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


def convertToHTMLString(hand):
    if len(hand) == 0:
        return 'Invalid Hand'
    x = []
    for card in hand:
        string = ''
        string += getCardSuitSymbol(card)
        string += card[0]
        x.append(string)
    return x