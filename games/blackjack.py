import deck
playerHand, houseHand = [], []
gameOver = False


def getTotal(hand):
    values = []
    for card in hand:
        if card[0] == 'A':
            values.append(11) if sum(values) < 11 else values.append(1)
        else:
            values.append(10) if card[0] in list('JQK') else values.append(int(card[0]))
    return sum(values)


def startOver():
    global playerHand, houseHand, gameOver
    gameOver = False
    playerHand, houseHand = [], []
    for i in range(2):
        houseHand.append(deck.getNewCard())
        playerHand.append(deck.getNewCard())
    if (getTotal(houseHand)) == 21:
        gameOver = True
        return 'House Wins with Blackjack'
    elif getTotal(playerHand) == 21:
        gameOver = True
        return 'You won with Blackjack!'


def checkWinLose():
    global gameOver
    # Dealer pulls cards until hard 17
    while getTotal(houseHand) < 16:
        houseHand.append(deck.getNewCard())
    if getTotal(playerHand) > 21:
        # Return player busted over 21
        gameOver = True
        return 'You busted, you lose.'
    elif getTotal(houseHand) > 21:
        # Return house busted over 21
        gameOver = True
        return 'The house busted, you win!'
    elif getTotal(playerHand) > getTotal(houseHand):
        # Return player won
        gameOver = True
        return 'You won!'
    else:
        # Return house won
        gameOver = True
        return 'You lost...'


def playerTurn(move):
    if getTotal(playerHand) < 21:
        if move == 'hit':
            playerHand.append(deck.getNewCard())


def convertToHTMLString(hand, houseCard=False):
    if not houseCard:
        return deck.convertDeckToHTMLString(hand)
    else:
        if len(hand) == 0:
            return 'Invalid Hand'
        x = []
        string = ''
        string += deck.getCardSuitSymbol(hand[0])
        string += hand[0][0]
        x.append(string)
        return x
