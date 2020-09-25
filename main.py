import Cardsv2
import time
from operator import attrgetter

def startbig2():
    deck = Cardsv2.Deck()
    deck.shuffle()
    player1.emptyhand()
    player2.emptyhand()
    player3.emptyhand()
    player4.emptyhand()

    print("Dealing cards")
    deck.deal(player1, deck, 13)
    deck.deal(player2, deck, 13)
    deck.deal(player3, deck, 13)
    deck.deal(player4, deck, 13)
    time.sleep(1)

def beginplaying(player):
    print(player.name + ", you have the 3 of Spades. Please begin!")
    ready = input("Please type 'ready' when you are ready!\n")
    if ready.lower() == "ready":
        firstplay(player)

def firstplay(player):
    global centerpile
    print("Sorting hand...")
    turndone = False
    lstofcards = []
    time.sleep(1)
    counthigher = 0
    countlower = 0
    countsame = 0
    player.sortHand()
    player.showHand()
    while True:
        print("Select the card to play (must be the starting card)\n")
        card_to_play_value = int(input("Enter the value:\n"))
        card_to_play_suit = input("Now enter the suit ('Spades', 'Clubs', 'Diamonds, 'Hearts'):\n")
        if card_to_play_suit.title() == "Spades":
            card_to_play_suit = 0
        elif card_to_play_suit.title() == "Clubs":
            card_to_play_suit = 1
        elif card_to_play_suit.title() == "Diamonds":
            card_to_play_suit = 2
        elif card_to_play_suit.title() == "Hearts":
            card_to_play_suit = 3
        card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
        if card_to_play_value == 3 and card_to_play_suit == 0:
            lstofcards.append(card_to_play)
            player.discard(card_to_play_value, card_to_play_suit)
            break
        else:
            print("Invalid choice, please pick the starting card (3 of Spades).")
    cardvalues = []
    for card in player.hand:
        if card.value == card_to_play.value:
            countsame += 1
        elif card.value == card_to_play.value + 1 and not (card.value in cardvalues):
            counthigher += 1
            cardvalues.append(card.value)
        elif counthigher >= 1 and card.value == card_to_play.value + 2:
            counthigher += 1
        elif card.value == card_to_play.value - 1 and not (card.value in cardvalues):
            countlower += 1
            cardvalues.append(card.value)
        elif countlower >= 1 and card.value == card_to_play.value - 2:
            countlower += 1
    if (counthigher > 1) or (countlower > 1) or (counthigher > 0 and countlower > 0) or countsame > 0:
        while turndone == False:
            anothercard = input("Would you like to play anything else? Type 'yes' or 'no'.\n")
            if anothercard == 'yes':
                while anothercard == 'yes':
                    if anothercard.lower() == 'yes':
                        card_to_play2_value = int(input("Enter the value:\n"))
                        card_to_play2_suit = input("Enter the suit:\n")
                        if card_to_play2_suit.title() == "Spades":
                            card_to_play2_suit = 0
                        elif card_to_play2_suit.title() == "Clubs":
                            card_to_play2_suit = 1
                        elif card_to_play2_suit.title() == "Diamonds":
                            card_to_play2_suit = 2
                        elif card_to_play2_suit.title() == "Hearts":
                            card_to_play2_suit = 3
                        card_to_play2 = Cardsv2.Card(card_to_play2_value, card_to_play2_suit)
                        if card_to_play2.value == lstofcards[0].value and card_to_play2 in player.hand:                                                                  #pairs, triples, quads
                            lstofcards.append(card_to_play2)
                            player.discard(card_to_play2.value, card_to_play2.suit)
                            availablecards = []
                            for card in player.hand:
                                if card.value == card_to_play2.value:
                                    availablecards.append(card)
                            if len(availablecards) == 0:
                                print("No other cards can be played, current list: ")
                                centerpile = lstofcards
                                print(player.name + " played: ")
                                print(centerpile)
                                turndone = True
                                break
                            else:
                                while True:
                                    print(availablecards)
                                    add_card = input("Would you like to add any of the above? ('yes' or 'no')\n")
                                    if add_card.lower() == "no":
                                        print("Playing Cards..")
                                        print(lstofcards)
                                        centerpile = lstofcards
                                        anothercard = 'no'
                                        turndone = True
                                        break
                                    elif add_card.lower() == "yes":
                                        cardsuit = input("Enter the card suit:\n")
                                        if cardsuit.title() == "Spades":
                                            cardsuit = 0
                                        elif cardsuit.title() == "Clubs":
                                            cardsuit = 1
                                        elif cardsuit.title() == "Diamonds":
                                            cardsuit = 2
                                        elif cardsuit.title() == "Hearts":
                                            cardsuit = 3
                                        cardtoadd = Cardsv2.Card(lstofcards[0].value, cardsuit)
                                        if cardtoadd in availablecards:
                                            lstofcards.append(cardtoadd)
                                            availablecards.remove(cardtoadd)
                                            player.discard(cardtoadd.value, cardtoadd.suit)
                                            if len(availablecards) == 0:
                                                anothercard = 'no'
                                                turndone = True
                                                break
                                        else:
                                            print("Invalid choice. Please type in a valid choice.")
                                    else:
                                        print("Invalid choice. Please enter in a valid choice.")
                        elif card_to_play2.value == lstofcards[0].value + 1 or card_to_play2.value == lstofcards[0].value - 1:                                                       #straights
                            max_cardvalue = max(lstofcards, key=attrgetter('value'))
                            min_cardvalue = min(lstofcards, key=attrgetter('value'))
                            availablecards = []
                            counthigher = 0
                            countlower = 0
                            for card in player.hand:
                                if card.value == max_cardvalue.value + 1:
                                    availablecards.append(card)
                                    counthigher += 1
                                if counthigher >= 1 and card.value == max_cardvalue.value + 2:
                                    counthigher += 1
                                if card.value == min_cardvalue.value - 1:
                                    availablecards.append(card)
                                    countlower += 1
                                if countlower >= 1 and card.value == min_cardvalue.value - 2:
                                    countlower += 1
                            if (counthigher > 0 and countlower > 0) or (card_to_play2.value == max_cardvalue.value + 1 and counthigher > 1) or (card_to_play2.value == min_cardvalue.value - 1 and countlower > 1):
                                lstofcards.append(card_to_play2)
                                player.discard(card_to_play2.value, card_to_play2.suit)
                                print("You need to add at least one more consecutive card for a valid play.\n")
                                choiceone = False
                                while choiceone == False:
                                    availablecards = []
                                    max_cardvalue = max(lstofcards, key=attrgetter('value'))
                                    min_cardvalue = min(lstofcards, key=attrgetter('value'))
                                    for card in player.hand:
                                        if card.value == max_cardvalue.value + 1 or card.value == min_cardvalue.value - 1:
                                            availablecards.append(card)
                                    print(availablecards)
                                    print("What card would you like to play?")
                                    card_to_play3_value = int(input('Enter the value:\n'))
                                    card_to_play3_suit = input('Enter the suit:\n')
                                    if card_to_play3_suit.title() == "Spades":
                                        card_to_play3_suit = 0
                                    elif card_to_play3_suit.title() == "Clubs":
                                        card_to_play3_suit = 1
                                    elif card_to_play3_suit.title() == "Diamonds":
                                        card_to_play3_suit = 2
                                    elif card_to_play3_suit.title() == "Hearts":
                                        card_to_play3_suit = 3
                                    card_to_play3 = Cardsv2.Card(card_to_play3_value, card_to_play3_suit)
                                    max_cardvalue = max(lstofcards, key=attrgetter('value'))
                                    min_cardvalue = min(lstofcards, key=attrgetter('value'))
                                    if (card_to_play3.value == max_cardvalue.value + 1 or card_to_play3.value == min_cardvalue.value - 1) and card_to_play3 in availablecards:
                                        lstofcards.append(card_to_play3)
                                        player.discard(card_to_play3.value, card_to_play3.suit)
                                        max_cardvalue = max(lstofcards, key=attrgetter('value'))
                                        min_cardvalue = min(lstofcards, key=attrgetter('value'))
                                        cardavailable = False
                                        availablecards = []
                                        for card in player.hand:
                                            if card.value == max_cardvalue.value + 1 or card.value == min_cardvalue.value - 1:
                                                cardavailable = True
                                                availablecards.append(card)
                                        if cardavailable:
                                            anothercard = input("Would you like to play another card? ('yes' or 'no')\n")
                                            if anothercard == 'yes':
                                                availablecards = []
                                            elif anothercard == 'no':
                                                centerpile = lstofcards
                                                print(player.name + " played:")
                                                print(centerpile)
                                                cardavailable = False
                                                choiceone = True
                                                turndone = True
                                            else:
                                                print("Invalid choice. Please enter in a valid choice.")
                                        else:
                                            print("No other cards available to play.")
                                            centerpile = lstofcards
                                            print(player.name + " played:")
                                            print(centerpile)
                                            choiceone = True
                                            turndone = True
                                            break
                                    else:
                                        print("Invalid choice. Please enter in a valid choice.")
                            else:
                                print("Invalid choice, you do not have the cards for a consecutive play.")
                        else:
                            print("Invalid choice. Please enter in a valid choice.")
            elif anothercard == 'no':
                centerpile = lstofcards
                print(player.name + " played: ")
                print(centerpile)
                turndone = True
            else:
                print("Invalid choice. Please print 'yes' or 'no'.")
    else:
        centerpile = lstofcards
        print("No other cards to play.")
        print(player.name + " played: ")
        print(centerpile)
        turndone = True

def playthrough(previous_player):
    global passcounter
    global centerpile
    global previousplayer
    currentplayer = None
    currentplayernum = previous_player.num + 1
    if currentplayernum == 5:
        currentplayernum = 1
    for player in players:
        if player.num == currentplayernum:
            currentplayer = player
    print(currentplayer.name + ", it's your turn!")

    #If all other players pass on the last card played
    if passcounter >= 3:
        passcounter = 0
        lstofcards = []
        centerpile = []
        print("Everyone has passed! Start fresh!")
        playerchoice = False
        while playerchoice == False:
            currentplayer.showHand()
            print("What card would you like to play?")
            card_to_play_value = input("Enter the card value:\n").title()
            if card_to_play_value == 'Ace':
                card_to_play_value = 14
            elif card_to_play_value == 'King':
                card_to_play_value = 13
            elif card_to_play_value == 'Queen':
                card_to_play_value = 12
            elif card_to_play_value == 'Jack':
                card_to_play_value = 11
            else:
                card_to_play_value = int(card_to_play_value)
            card_to_play_suit = input("Enter the card suit:\n").title()
            if card_to_play_suit == "Spades":
                card_to_play_suit = 0
            elif card_to_play_suit == "Clubs":
                card_to_play_suit = 1
            elif card_to_play_suit == "Diamonds":
                card_to_play_suit = 2
            elif card_to_play_suit == "Hearts":
                card_to_play_suit = 3
            card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
            if card_to_play in currentplayer.hand:
                lstofcards.append(card_to_play)
                currentplayer.discard(card_to_play.value, card_to_play.suit)
                countsame = 0
                counthigher = 0
                countlower = 0
                cardvalues = []
                for card in currentplayer.hand:
                    if card.value == card_to_play.value:
                        countsame += 1
                    elif card.value == card_to_play.value + 1 and not (card.value in cardvalues):
                        counthigher += 1
                        cardvalues.append(card.value)
                    elif counthigher >= 1 and card.value == card_to_play.value + 2:
                        counthigher += 1
                    elif card.value == card_to_play.value - 1 and not (card.value in cardvalues):
                        countlower += 1
                        cardvalues.append(card.value)
                    elif countlower >= 1 and card.value == card_to_play.value - 2:
                        countlower += 1
                if (counthigher > 1) or (countlower > 1) or (counthigher > 0 and countlower > 0) or countsame > 0:
                    playerchoice2 = False
                    while playerchoice2 == False:
                        currentplayer.sortHand()
                        anothercard = input("Would you like to play anything else? (Type in 'yes' or 'no')\n")
                        if anothercard == 'yes':
                            currentplayer.showHand()
                            print("What card would you like to play?")
                            card_to_play_value = input("Enter the value:\n").title()
                            if card_to_play_value == 'Ace':
                                card_to_play_value = 14
                            elif card_to_play_value == 'King':
                                card_to_play_value = 13
                            elif card_to_play_value == 'Queen':
                                card_to_play_value = 12
                            elif card_to_play_value == 'Jack':
                                card_to_play_value = 11
                            else:
                                card_to_play_value = int(card_to_play_value)
                            card_to_play_suit = input("Enter the card suit:\n")
                            if card_to_play_suit.title() == "Spades":
                                card_to_play_suit = 0
                            elif card_to_play_suit.title() == "Clubs":
                                card_to_play_suit = 1
                            elif card_to_play_suit.title() == "Diamonds":
                                card_to_play_suit = 2
                            elif card_to_play_suit.title() == "Hearts":
                                card_to_play_suit = 3
                            card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
                            if card_to_play in currentplayer.hand and (card_to_play.value == lstofcards[0].value or card_to_play_value == lstofcards[0].value + 1 or card_to_play_value == lstofcards[0].value - 1):
                                lstofcards.append(card_to_play)
                                currentplayer.discard(card_to_play.value, card_to_play.suit)
                                playerchoice2 = True
                                availablecards =[]
                                if card_to_play.value == lstofcards[0].value and card_to_play in currentplayer.hand:
                                    for card in currentplayer.hand:
                                        if card.value == card_to_play.value:
                                            availablecards.append(card)
                                    if len(availablecards) == 0:
                                        print("No other cards to play.")
                                        centerpile = lstofcards
                                        print(currentplayer.name + " played: ")
                                        print(centerpile)
                                        playerchoice = True
                                    else:
                                        playerchoice3 = False
                                        while playerchoice3 == False:
                                            print(availablecards)
                                            print("Would you like to play any of the above cards?")
                                            card_to_play_value = input("Enter the value or 'no':\n").title()
                                            if card_to_play_value == 'Ace':
                                                card_to_play_value = 14
                                            elif card_to_play_value == 'King':
                                                card_to_play_value = 13
                                            elif card_to_play_value == 'Queen':
                                                card_to_play_value = 12
                                            elif card_to_play_value == 'Jack':
                                                card_to_play_value = 11
                                            elif card_to_play_value == "No":
                                                print("No other cards played.")
                                                centerpile = lstofcards
                                                print(currentplayer.name + " played: ")
                                                print(centerpile)
                                                playerchoice = True
                                                break
                                            else:
                                                card_to_play_value = int(card_to_play_value)
                                            card_to_play_suit = input("Enter the suit:\n")
                                            if card_to_play_suit.title() == "Spades":
                                                card_to_play_suit = 0
                                            elif card_to_play_suit.title() == "Clubs":
                                                card_to_play_suit = 1
                                            elif card_to_play_suit.title() == "Diamonds":
                                                card_to_play_suit = 2
                                            elif card_to_play_suit.title() == "Hearts":
                                                card_to_play_suit = 3
                                            card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
                                            if card_to_play in availablecards:
                                                availablecards.remove(card_to_play)
                                                currentplayer.discard(card_to_play.value, card_to_play.suit)
                                                lstofcards.append(card_to_play)
                                                if len(availablecards) == 0:
                                                    playerchoice3 = True
                                                    centerpile = lstofcards
                                                    print("No other cards can be played.")
                                                    print(currentplayer.name + " played: ")
                                                    print(centerpile)
                                                    playerchoice = True
                                                else:
                                                    playerchoice4 = False
                                                    while playerchoice4 == False:
                                                        anothercard2 = input("Would you like to play any other cards?")
                                                        if anothercard2 == 'yes':
                                                            playerchoice4 = True
                                                        elif anothercard2 == 'no':
                                                            playerchoice = True
                                                            playerchoice3 = True
                                                            playerchoice4 = True
                                                            centerpile = lstofcards
                                                            print(currentplayer.name + " played: ")
                                                            print(centerpile)
                                                        else:
                                                            print("Invalid choice. Type 'yes' or 'no'.")
                                            else:
                                                print("Card entered not a viable play.")
                                elif card_to_play.value == lstofcards[0].value + 1 or card_to_play.value == lstofcards[0].value - 1 and card_to_play in currentplayer.hand:
                                    currentplayer.discard(card_to_play.value, card_to_play.suit)
                                    print("You will need to play at least one more card for a valid straight play.")
                                    playerchoice3 = False
                                    while playerchoice3 == False:
                                        availablecards = []
                                        maxcard = max(lstofcards, key=attrgetter('value'))
                                        mincard = min(lstofcards, key=attrgetter('value'))
                                        for card in currentplayer.hand:
                                            if card.value == maxcard.value + 1 or card.value == mincard.value - 1:
                                                availablecards.append(card)
                                        if len(availablecards) == 0:
                                            print("No other cards can be played.")
                                            print("Resetting..")
                                            for card in lstofcards:
                                                currentplayer.hand.append(card)
                                            playerchoice3 = True
                                        else:
                                            playerchoice4 = False
                                            while playerchoice4 == False:
                                                print(availablecards)
                                                print("What card would you like to play?")
                                                card_to_play_value = input("Enter the card value:\n").title()
                                                if card_to_play_value == 'Ace':
                                                    card_to_play_value = 14
                                                elif card_to_play_value == 'King':
                                                    card_to_play_value = 13
                                                elif card_to_play_value == 'Queen':
                                                    card_to_play_value = 12
                                                elif card_to_play_value == 'Jack':
                                                    card_to_play_value = 11
                                                else:
                                                    card_to_play_value = int(card_to_play_value)
                                                card_to_play_suit = input("Enter the card suit:\n").title()
                                                if card_to_play_suit.title() == "Spades":
                                                    card_to_play_suit = 0
                                                elif card_to_play_suit.title() == "Clubs":
                                                    card_to_play_suit = 1
                                                elif card_to_play_suit.title() == "Diamonds":
                                                    card_to_play_suit = 2
                                                elif card_to_play_suit.title() == "Hearts":
                                                    card_to_play_suit = 3
                                                card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
                                                if card_to_play in availablecards:
                                                    playerchoice4 = True
                                                    currentplayer.discard(card_to_play.value, card_to_play.suit)
                                                    lstofcards.append(card_to_play)
                                                    playerchoice5 = False
                                                    while playerchoice5 == False:
                                                        anothercard3 = input("Would you like to play another card? (Type 'yes' or 'no')\n").lower()
                                                        if anothercard3 == "yes":
                                                            playerchoice6 = False
                                                            while playerchoice6 == False:
                                                                availablecards = []
                                                                maxcard = max(lstofcards, key=attrgetter('value'))
                                                                mincard = min(lstofcards, key=attrgetter('value'))
                                                                for card in currentplayer.hand:
                                                                    if card.value == maxcard.value + 1 or card.value == mincard.value - 1:
                                                                        availablecards.append(card)
                                                                if len(availablecards) == 0:
                                                                    print("No other card to be played!")
                                                                    centerpile = lstofcards
                                                                    print(currentplayer.name + " played:")
                                                                    print(centerpile)
                                                                    playerchoice6 = True
                                                                    playerchoice5 = True
                                                                    playerchoice4 = True
                                                                    playerchoice3 = True
                                                                    playerchoice2 = True
                                                                    playerchoice = True
                                                                else:
                                                                    playerchoice7 = False
                                                                    while playerchoice7 == False:
                                                                        print(availablecards)
                                                                        print("What card would you like to play?")
                                                                        card_to_play_value = input(
                                                                            "Enter the card value:\n").title()
                                                                        if card_to_play_value == 'Ace':
                                                                            card_to_play_value = 14
                                                                        elif card_to_play_value == 'King':
                                                                            card_to_play_value = 13
                                                                        elif card_to_play_value == 'Queen':
                                                                            card_to_play_value = 12
                                                                        elif card_to_play_value == 'Jack':
                                                                            card_to_play_value = 11
                                                                        else:
                                                                            card_to_play_value = int(card_to_play_value)
                                                                        card_to_play_suit = input(
                                                                            "Enter the card suit:\n").title()
                                                                        if card_to_play_suit.title() == "Spades":
                                                                            card_to_play_suit = 0
                                                                        elif card_to_play_suit.title() == "Clubs":
                                                                            card_to_play_suit = 1
                                                                        elif card_to_play_suit.title() == "Diamonds":
                                                                            card_to_play_suit = 2
                                                                        elif card_to_play_suit.title() == "Hearts":
                                                                            card_to_play_suit = 3
                                                                        card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
                                                                        if card_to_play in availablecards:
                                                                            lstofcards.append(card_to_play)
                                                                            currentplayer.discard(card_to_play.value, card_to_play.suit)
                                                                            playerchoice7 = True
                                                                            playerchoice6 = True
                                                                        else:
                                                                            print("Invalid choice. Please select an option on the list of cards to play.")

                                                        elif anothercard3 == "no":
                                                            centerpile = lstofcards
                                                            print(currentplayer.name + " played:")
                                                            print(centerpile)
                                                            playerchoice5 = True
                                                            playerchoice3 = True
                                                            playerchoice4 = True
                                                            playerchoice2 = True
                                                            playerchoice = True
                                                        else:
                                                            print("Invalid choice. Please type in 'yes' or 'no'.")
                                                else:
                                                    print("Not a valid play. Card not an available card to play.")

                                        #############################################################
                                else:
                                    print("Not a valid play. Try again.")
                                    print("If you are trying to play a straight, you will need to play it in order")
                            else:
                                print('Not a valid play with your first card. Try again.')
                                print('If you are trying to play a straight, you will need to play it in order.')

        #############################################################################################
                        elif anothercard == 'no':
                            centerpile = lstofcards
                            print(currentplayer.name + " played: ")
                            print(centerpile)
                            playerchoice = True
                        else:
                            print("Invalid response. Just type 'yes' or 'no'.")
                else:
                    centerpile = lstofcards
                    print("No other cards can be played.")
                    print(currentplayer.name + " played: ")
                    print(centerpile)
                    playerchoice = True
            else:
                print("Card not in hand. Choose another card.")
    ################################################################
    else:
        single_play = False
        triple_play = False
        double_play = False
        quad_play = False
        straight_var = False
        #full_house = False #not coded yet
        #chop_play = False #not coded yet

        #Determining the previous play
        sortedcenterpile = sorted(centerpile, key=attrgetter('value'))
        if len(sortedcenterpile) >= 3 and sortedcenterpile[0].value + 1 == sortedcenterpile[1].value and sortedcenterpile[1].value + 1 == sortedcenterpile[2].value:
            straight_var = True
        elif len(sortedcenterpile) == 4 and sortedcenterpile[0].value == sortedcenterpile[3].value:
            quad_play = True
        elif len(sortedcenterpile) == 3 and sortedcenterpile[0].value == sortedcenterpile[2].value:
            triple_play = True
        elif len(sortedcenterpile) == 2 and sortedcenterpile[0].value == sortedcenterpile[1].value:
            double_play = True
        elif len(sortedcenterpile) == 1:
            single_play = True

        playerchoice = False
        while playerchoice == False:
            readystatus = input(currentplayer.name + " type 'ready' when you are ready!\n")
            if readystatus.lower() == 'ready':
                playerchoice = True
                playerchoice2 = False
                while playerchoice2 == False:
                    print("The center currently is: ")
                    print(centerpile)
                    time.sleep(1)
                    currentplayer.sortHand()
                    currentplayer.showHand()
                    playstatus = input("Would you like to 'play' or 'pass'?\n")
                    if playstatus.lower() == 'play':
                        lstofcards = []
                        playerchoice3 = False
                        while playerchoice3 == False:
                            maxcentercard = max(centerpile, key=attrgetter('value'))
                            print("Which card would you like to play?")
                            print("If the previous player had played multiple cards, you must start with your highest card in the combo.")
                            card_to_play_value = input("Enter the card's value or 'pass' to pass:\n")
                            if card_to_play_value.title() == 'Ace':
                                card_to_play_value = 14
                            elif card_to_play_value.title() == 'King':
                                card_to_play_value = 13
                            elif card_to_play_value.title() == 'Queen':
                                card_to_play_value = 12
                            elif card_to_play_value.title() == 'Jack':
                                card_to_play_value = 11
                            elif card_to_play_value.title() == 'Pass':
                                playerchoice2 = True
                                playerchoice3 = True
                                print(currentplayer.name + " has passed! Moving on to next player..")
                            else:
                                card_to_play_value = int(card_to_play_value)
                            card_to_play_suit = input("Enter the card's suit:\n")
                            if card_to_play_suit.title() == "Spades":
                                card_to_play_suit = 0
                            elif card_to_play_suit.title() == "Clubs":
                                card_to_play_suit = 1
                            elif card_to_play_suit.title() == "Diamonds":
                                card_to_play_suit = 2
                            elif card_to_play_suit.title() == "Hearts":
                                card_to_play_suit = 3
                            card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
                            if card_to_play in currentplayer.hand and (card_to_play.value > maxcentercard.value or (card_to_play_value == maxcentercard.value and card_to_play.suit > maxcentercard.suit)):
                                lstofcards.append(card_to_play)
                                currentplayer.discard(card_to_play.value, card_to_play.suit)

                                if single_play == True:
                                    centerpile = lstofcards
                                    print(currentplayer.name + " played: ")
                                    print(centerpile)
                                    playerchoice2 = True
                                    playerchoice = True
                                    break

                                elif double_play == True:
                                    maxcentercard = max(centerpile, key=attrgetter('suit'))
                                    availablecards = []
                                    for card in currentplayer.hand:
                                        if card.value == card_to_play.value:
                                            availablecards.append(card)
                                    if len(availablecards) == 0:
                                        print("No other card to play with your selected card.")
                                        print("Please reselect a card for a valid play.")
                                        playerchoice3 = True
                                        for card in lstofcards:
                                            currentplayer.hand.append(card)
                                    else:
                                        playerchoice4 = False
                                        while playerchoice4 == False:
                                            print("Please select a card to play from below:")
                                            print(availablecards)
                                            card_to_play_value = input("Enter a value:\n").title()
                                            if card_to_play_value == 'Ace':
                                                card_to_play_value = 14
                                            elif card_to_play_value == 'King':
                                                card_to_play_value = 13
                                            elif card_to_play_value == 'Queen':
                                                card_to_play_value = 12
                                            elif card_to_play_value == 'Jack':
                                                card_to_play_value = 11
                                            elif card_to_play_value == 'Pass':
                                                print(currentplayer.name + " has passed!")
                                                playerchoice = True
                                                playerchoice2 = True
                                                playerchoice3 = True
                                                for card in lstofcards:
                                                    currentplayer.hand.append(card)
                                                passcounter += 1
                                                break
                                            else:
                                                card_to_play_value = int(card_to_play_value)
                                            card_to_play_suit = input("Enter a suit:\n")
                                            if card_to_play_suit.title() == "Spades":
                                                card_to_play_suit = 0
                                            elif card_to_play_suit.title() == "Clubs":
                                                card_to_play_suit = 1
                                            elif card_to_play_suit.title() == "Diamonds":
                                                card_to_play_suit = 2
                                            elif card_to_play_suit.title() == "Hearts":
                                                card_to_play_suit = 3
                                            card_to_play = Cardsv2.Card(card_to_play_value, card_to_play_suit)
                                            if card_to_play in availablecards and card_to_play.value == lstofcards[0].value:
                                                lstofcards.append(card_to_play)
                                                currentplayer.discard(card_to_play.value, card_to_play.suit)
                                                maxlstofcard = max(lstofcards, key=attrgetter('suit'))
                                                if maxlstofcard.value > maxcentercard.value:
                                                    centerpile = lstofcards
                                                    print(currentplayer.name + "played: ")
                                                    print(centerpile)
                                                    playerchoice = True
                                                    playerchoice2 = True
                                                    playerchoice3 = True
                                                    playerchoice4 = True
                                                elif maxlstofcard.value == maxcentercard.value and maxlstofcard.suit > maxcentercard.value:
                                                    centerpile = lstofcards
                                                    print(currentplayer.name + "played: ")
                                                    print(centerpile)
                                                    playerchoice = True
                                                    playerchoice2 = True
                                                    playerchoice3 = True
                                                    playerchoice4 = True
                                                else:
                                                    print("Invalid play. Your highest played card's suit is too low")
                                                    print("Rule: Hearts > Diamonds > Clubs > Spades")
                                                    print("Resetting cards..")
                                                    for card in lstofcards:
                                                        currentplayer.hand.append(card)
                                                    playerchoice3 = True
                                                    playerchoice4 = True
                                            else:
                                                print("Invalid play. Card not in hand or a real card.")
                                    ################################################

                                elif triple_play == True:
                                    continue
                                ################################
                                elif quad_play == True:
                                    continue
                                #############################
                                elif straight_var == True:
                                    continue
                                #############################
                            else:
                                print("Invalid play. Card not in hand or card just doesn't exist.")
                    elif playstatus.lower() == 'pass':
                        playerchoice2 = True
                        playerchoice = True
                        passcounter += 1
                        print(currentplayer.name + " has passed! Moving on to next player..")
                    else:
                        print("Invalid Response, please enter 'play' or 'pass'.")
            else:
                print("Invalid Response, please type 'ready' if you are ready.")
    previousplayer = currentplayer


print('Welcome to Big 2!')
player1_name = input("Player 1, what is your name?\n")
player2_name = input("Player 2, what is your name?\n")
player3_name = input("Player 3, what is your name?\n")
player4_name = input("Player 4, what is your name?\n")
print("Alright, now that everyone's here, let's play!")

print("Setting up game...")
player1 = Cardsv2.Player(player1_name, num=1)
player2 = Cardsv2.Player(player2_name, num=2)
player3 = Cardsv2.Player(player3_name, num=3)
player4 = Cardsv2.Player(player4_name, num=4)
players = [player1, player2, player3, player4]
passcounter = 0
centerpile = []

while player1.in_play and player2.in_play and player3.in_play and player4.in_play:
    startbig2()
    starting_card = Cardsv2.Card(3, 0)

    while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(player4.hand) != 0:
        if starting_card in player1.hand:
            beginplaying(player1)
            previousplayer = player1
            while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(
                    player4.hand) != 0:
                playthrough(previousplayer)
        elif starting_card in player2.hand:
            beginplaying(player2)
            previousplayer = player2
            while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(
                    player4.hand) != 0:
                playthrough(previousplayer)
        elif starting_card in player3.hand:
            beginplaying(player3)
            previousplayer = player3
            while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(
                    player4.hand) != 0:
                playthrough(previousplayer)
        elif starting_card in player4.hand:
            beginplaying(player4)
            previousplayer = player4
            while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(
                    player4.hand) != 0:
                playthrough(previousplayer)
