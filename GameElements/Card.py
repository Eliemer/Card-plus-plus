class Card(object):

    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    valueList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def printCard(self):
        return self.valueList[self.value] + "of" + self.suitList[self.suit] + "\n"

    def compCardValues(self, other):
        if self.value > other.value:
            return 1
        if self.value < other.value:
            return -1
        return 0

    def compCardSuits(self, other):
        if self.suit == other.suit:
            return 1
        return -1




