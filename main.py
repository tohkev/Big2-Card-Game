import Cards
import time
from operator import attrgetter

def startbig2():
    deck = Cards.Deck()
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
        card_to_play = Cards.Card(card_to_play_value, card_to_play_suit.title())
        if card_to_play.value == 3 and card_to_play.suit.title() == "Spades":
            lstofcards.append(card_to_play)
            player.discard(card_to_play.value, card_to_play.suit)
            break
        else:
            print("Invalid choice, please pick the starting card (3 of Spades).")
    for card in player.hand:
        if card.value == card_to_play.value:
            countsame += 1
        elif card.value == card_to_play.value + 1:
            counthigher += 1
        elif card.value == card_to_play.value - 1:
            countlower += 1
    if (counthigher > 0 and countlower > 0) or countsame > 0:
        while turndone == False:
            anothercard = input("Would you like to play anything else? Type 'yes' or 'no'.\n")
            if anothercard == 'yes':
                while anothercard == 'yes':
                    if anothercard.lower() == 'yes':
                        card_to_play_value = int(input("Enter the value:\n"))
                        card_to_play_suit = input("Enter the suit:\n")
                        card_to_play2 = Cards.Card(card_to_play_value, card_to_play_suit.title())
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
                                        cardtoadd = Cards.Card(lstofcards[0].value, cardsuit.title())
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
                                if countlower >= 1 and card.value == min_cardvalue.value - 1:
                                    countlower += 1
                            if counthigher > 0 and countlower > 0:
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
                                    card_to_play3 = Cards.Card(card_to_play3_value, card_to_play3_suit.title())
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
    currentplayer = None
    currentplayernum = previous_player.num + 1
    if currentplayernum == 5:
        currentplayernum = 1
    for player in players:
        if player.num == currentplayernum:
            currentplayer = player
    print(currentplayer.name + ", it's your turn!")
    playerchoice = False
    while playerchoice == False:
        readystatus = input("Type 'ready' when you are ready!\n")
        playerchoice = True
        if readystatus.lower() == 'ready':
            playerchoice = True
            playerchoice2 = False
            while playerchoice2 == False:
                print("The center currently is: ")
                print(centerpile)
                playstatus = input("Would you like to 'play' or 'pass'?")
                if playstatus.lower() == 'play':
                    print("You will need to play: " + str(len(centerpile)) + " cards.")
                    playerchoice2 = True
                    lstofcards = []
                    playerchoice3 = False
                    while playerchoice3 == False:
                        currentplayer.showHand()
                        print("Which card would you like to play?")
                        print("If the previous player had played multiple cards, you must start with your highest card in the combo.")
                        card_to_play_value = input("Enter the card's value or 'pass' to pass:\n").title()
                        if card_to_play_value == 'Ace':
                            card_to_play_value = 14
                        elif card_to_play_value == 'King':
                            card_to_play_value = 13
                        elif card_to_play_value == 'Queen':
                            card_to_play_value = 12
                        elif card_to_play_value == 'Jack':
                            card_to_play_value = 11
                        elif card_to_play_value == 'Pass':
                            playerchoice2 = True
                            print(currentplayer.name + " has passed! Moving on to next player..")
                        else:
                            card_to_play_value = int(card_to_play_value)
                        card_to_play_suit = input("Enter the card's suit:\n")
                        card_to_play = Cards.Card(card_to_play_value, card_to_play_suit)
                        if card_to_play in currentplayer.hand:
                            playerchoice3 = True
                            lstofcards.append(card_to_play)
                            ###################to be continued####################
                        else:
                            print("Invalid choice. Not a viable play, in your hand, or a real card.")


                elif playstatus.lower() == 'pass':
                    playerchoice2 = True
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
player1 = Cards.Player(player1_name, num=1)
player2 = Cards.Player(player2_name, num=2)
player3 = Cards.Player(player3_name, num=3)
player4 = Cards.Player(player4_name, num=4)
players = [player1, player2, player3, player4]

while player1.in_play and player2.in_play and player3.in_play and player4.in_play:
    startbig2()
    centerpile = []
    starting_card = Cards.Card(3, "Spades")

    while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(player4.hand) != 0:
        if starting_card in player1.hand:
            beginplaying(player1)
            previousplayer = player1
            while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(player4.hand) != 0:
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
