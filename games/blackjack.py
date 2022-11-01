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
    global gameOver
    global playerHand, houseHand
    playerHand, houseHand = [], []
    gameOver = False
    for i in range(2):
        houseHand.append(deck.getNewCard())
        playerHand.append(deck.getNewCard())
    # Return the starting cards
    # print(f'Total is {getTotal(playerHand)} Your cards are {playerHand}. The Dealers card is {houseHand[0]}')
    if (getTotal(houseHand)) == 21:
        return 'House Wins with Blackjack'
    elif getTotal(playerHand) == 21:
        return 'You won with Blackjack!'
    return ''


def checkWinLose():
    # Dealer pulls cards until hard 17
    while getTotal(houseHand) < 16:
        houseHand.append(deck.getNewCard())
    if getTotal(playerHand) > 21:
        # Return player busted over 21
        return 'You busted, you lose.'
    elif getTotal(houseHand) > 21:
        # Return house busted over 21
        return 'The house busted, you win!'
    elif getTotal(playerHand) > getTotal(houseHand):
        # Return player won
        return 'You won!'
    else:
        # Return house won
        return 'You lost...'


def playerTurn(move):
    if not gameOver:
        if getTotal(playerHand) < 21:
            if move == 'hit':
                playerHand.append(deck.getNewCard())


def convertToHTMLString(hand):
    x = ''
    for card in hand:
        x += card[0]
        x += deck.getCardSuitSymbol(card)
    return x
