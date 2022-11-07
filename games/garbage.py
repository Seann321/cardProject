playerHand = []
AIHand = []
playerCardCount = 10
cardSelected = list()
for i in range(playerCardCount):
    playerHand.append('0')


# Resets everything according to x amount of cards in the hand
def restart(cardCount=10):
    global playerHand, AIHand, playerCardCount, cardSelected
    playerHand = []
    AIHand = []
    playerCardCount = cardCount
    cardSelected = list()
    for x in range(playerCardCount):
        playerHand.append('0')


# Setter for cardSelected
def choiceNewCard(card):
    global cardSelected
    cardSelected = list(card)


# Check if the card selected can be swapped with the card in hand
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


# If there are no more unknown cards in a deck, return True
def checkForWin():
    for x in playerHand:
        if x[0] == '0':
            return False
    return True
