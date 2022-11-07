playerHand = []
AIHand = []
discardedCard = []
playerCardCount = 10
cardSelected = list()
for i in range(playerCardCount):
    playerHand.append('0')


# Resets everything according to x amount of cards in the hand
def restart(cardCount=10):
    global playerHand, AIHand, playerCardCount, cardSelected, discardedCard
    playerHand = []
    AIHand = []
    discardedCard = []
    playerCardCount = cardCount
    cardSelected = list()
    for x in range(playerCardCount):
        playerHand.append('0')


# Discard card and end your turn
def discardCard():
    global discardedCard, cardSelected
    if len(cardSelected) == 0:
        return False
    discardedCard = cardSelected
    cardSelected = list()


# Sets the selected card to the card in the discarded pile
def pullFromDiscard():
    global discardedCard, cardSelected
    if len(discardedCard) == 0:
        return False
    cardSelected = discardedCard
    discardedCard = list()


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
