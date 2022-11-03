import deck
playerHand = []
AIHand = []
playerCardCount = 10


def startNewGame():
    playerHand.clear()
    global playerCardCount
    playerCardCount = 10
    for i in range(10):
        playerHand.append(deck.getNewCard())


def pickCard(cardSpot):
    if playerHand[cardSpot][0] in list('QJ'):
        print('Garbage')

