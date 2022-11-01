from itertools import product
from random import shuffle
deck = []


def shuffleDeck():
    global deck
    cardValues = list(range(2, 11)) + list('JQKA')
    deck = [x for x in product([str(cardValue) for cardValue in cardValues], ['Spades', 'Hearts', 'Clubs', 'Diamonds'])]
    shuffle(deck)


def getTotal(hand):
    values = []
    for card in hand:
        if card[0] == 'A':
            values.append(11) if sum(values) < 11 else values.append(1)
        else:
            values.append(10) if card[0] in list('JQK') else values.append(int(card[0]))
    return sum(values)


def getNewCard():
    if len(deck) == 0:
        print('Shuffling Deck')
        shuffleDeck()
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
