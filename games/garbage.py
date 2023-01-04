import deck

playerHand = []
AIHand = []
discardedCard = []
playerCardCount = 10
AICardCount = 10
cardSelected = list()
AICardSelected = list()
for i in range(playerCardCount):
    playerHand.append('0')
for x in range(AICardCount):
    AIHand.append('0')


# Resets everything according to x amount of cards in the hand
def restart(playerCount=10, AICount=10):
    global playerHand, AIHand, playerCardCount, cardSelected, discardedCard, AICardCount, AICardSelected
    playerHand = []
    AIHand = []
    discardedCard = []
    playerCardCount = playerCount
    AICardCount = AICount
    cardSelected = list()
    AICardSelected = list()
    for x in range(playerCardCount):
        playerHand.append('0')
    for x in range(AICardCount):
        AIHand.append('0')


# AI Turn, Is triggered when player discards their card
def computersTurn():
    global AICardSelected, discardedCard, AICardCount
    if len(discardedCard) == 0 or discardedCard[0] in list('QJ'):
        AICardSelected = list(deck.getNewCard())
    elif discardedCard[0] in list('K'):
        AICardSelected = discardedCard
        discardedCard = list()
    elif discardedCard[0] in list('A'):
        if AIHand[0][0] != '0':
            AICardSelected = list(deck.getNewCard())
        else:
            AICardSelected = discardedCard
            discardedCard = list()
    elif int(discardedCard[0]) > AICardCount:
        AICardSelected = list(deck.getNewCard())
    else:
        # Make sure card isn't needed
        for card in AIHand:
            if card[0] == discardedCard[0]:
                discardedCard = list(deck.getNewCard())
        AICardSelected = discardedCard
        discardedCard = list()
    computerTurns()
    # No more moves, discards card.
    discardedCard = AICardSelected
    AICardSelected = list()
    if '0' not in AIHand:
        print('Computer win')
        AICardCount -= 1
        restart(playerCardCount, AICardCount)
    return False


# Plays until there are no more valid moves
def computerTurns():
    global AICardSelected, discardedCard
    if AICardSelected[0] not in list('AQJK'):
        # Looks for valid moves to play.
        if int(AICardSelected[0]) > AICardCount:
            return
        elif AIHand[int(AICardSelected[0]) - 1][0] == '0':
            AIHand[int(AICardSelected[0]) - 1] = AICardSelected
            AICardSelected = deck.getNewCard()
            computerTurns()
    elif AICardSelected[0] == 'A':
        if AIHand[0][0] == '0':
            AIHand[0] = AICardSelected
            AICardSelected = deck.getNewCard()
            computerTurns()
    elif AICardSelected[0] == 'K':
        for spot in AIHand:
            if spot[0] == '0':
                AIHand[AIHand.index(spot)] = AICardSelected
                AICardSelected = deck.getNewCard()
                computerTurns()
                return
        return


# Discard card and end your turn
def discardCard():
    global discardedCard, cardSelected
    if len(cardSelected) == 0:
        return False
    discardedCard = cardSelected
    cardSelected = list()
    computersTurn()


# Sets the selected card to the card in the discarded pile
def pullFromDiscard():
    global discardedCard, cardSelected
    if len(discardedCard) == 0:
        return False
    if len(cardSelected) != 0:
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
