import random
from operator import attrgetter                                     #used to sort cards

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        if self.value == 14:
            self.value = "Ace"
        elif self.value == 13:
            self.value = "King"
        elif self.value == 12:
            self.value = "Queen"
        elif self.value == 11:
            self.value = "Jack"
        return "{} of {}". format(self.value, self.suit)

    def __eq__(self, other):                                        #used to compare cards
        if self.suit == other.suit and self.value == other.value:
            return True

    def show(self):
        print("{} of {}". format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for value in range(2, 15):
                self.cards.append(Card(value, suit))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def deal(self, Player, deck, num_draw):
        for i in range(num_draw):
            Player.hand.append(deck.drawCard())

class Player:
    def __init__(self, name, in_play=True, num=0):
        self.name = name
        self.hand = []
        self.in_play = in_play
        self.win = 0
        self.num = num

    def __repr__(self):
        return self.name

    def draw(self):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            if card.value == 11:
                card.value = "Jack"
            elif card.value == 12:
                card.value = "Queen"
            elif card.value == 13:
                card.value = "King"
            elif card.value == 14:
                card.value = "Ace"
            card.show()

    def checkwins(self):
        print("You have " + str(self.win) + " wins!")

    def sortHand(self):
        sorted_player_hand = sorted(self.hand, key=attrgetter('value'))
        self.hand = sorted_player_hand

    def discard(self, value, suit):
        for card in self.hand:
            if card.value == value and card.suit == suit.title():
                self.hand.remove(card)

    def emptyhand(self):
        self.hand = []
