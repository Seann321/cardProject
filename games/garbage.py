playerHand = []
AIHand = []
playerCardCount = 10
cardSelected = list()
for i in range(playerCardCount):
    playerHand.append('0')


def restart(cardCount=10):
    global playerHand, AIHand, playerCardCount, cardSelected
    playerHand = []
    AIHand = []
    playerCardCount = cardCount
    cardSelected = list()
    for x in range(playerCardCount):
        playerHand.append('0')


def choiceNewCard(card):
    global cardSelected
    cardSelected = list(card)


def switchCardsValid(card):
    cardValue = cardSelected[0]
    if cardValue == 'A':
        cardValue = '1'
    if cardValue in list('QJ'):
        return False
    elif cardValue == 'K':
        return True
    elif card + 1 == int(cardValue):
        return True
    else:
        return False
