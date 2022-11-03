import deck
playerHand = []
AIHand = []
playerCardCount = 10


def startNewGame():
    global playerCardCount, playerHand
    playerHand.clear()
    playerCardCount = 10
    for i in range(playerCardCount):
        playerHand.append('0')


def pickCard(cardSpot):
    if playerHand[cardSpot][0] in list('QJ'):
        print('Garbage')

