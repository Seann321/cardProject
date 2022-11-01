import deck
deck = deck.deck


def getTotal(hand):
    values = []
    for card in hand:
        if card[0] == 'A':
            values.append(11) if sum(values) < 11 else values.append(1)
        else:
            values.append(10) if card[0] in list('JQK') else values.append(int(card[0]))
    return sum(values)


while True:
    playerHand, houseHand = [], []
    print('Welcome To BlackJack')
    for i in range(2):
        houseHand.append(deck.getNewCard())
        playerHand.append(deck.getNewCard())
    # Return the starting cards
    # print(f'Total is {getTotal(playerHand)} Your cards are {playerHand}. The Dealers card is {houseHand[0]}')
    if (getTotal(houseHand)) == 21:
        break
        # If the house wins with Blackjack return
        # print('House wins with Blackjack')
    elif getTotal(playerHand) == 21:
        break
        # If the player wins with Blackjack return
        # print('You win with Blackjack!')
    else:
        while getTotal(playerHand) < 21:
            # Get player choice of hit, stand, or split.
            break
        # Dealer pulls cards until hard 17
        while getTotal(houseHand) < 16:
            houseHand.append(deck.getNewCard())
        if getTotal(playerHand) > 21:
            # Return player busted over 21
            break
        elif getTotal(houseHand) > 21:
            # Return house busted over 21
            break
        elif getTotal(playerHand) > getTotal(houseHand):
            # Return player won
            break
        else:
            # Return house won
            break
    print()