class Card(object):

    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    valueList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.facedown = False

    def flip(self):
        self.facedown = not self.facedown

    def getValue(self):
        if(not self.facedown):
            return self.value
        else:
            return "***"

    def getSuit(self):
        if (not self.facedown):
            return self.suit
        else:
            return "***"

    def setValue(self, value):
        self.value = value

    def setSuit(self, suit):
        self.suit = suit

    def printCard(self):
        if self.facedown == 0:
            return "(" + self.valueList[self.value] + ", " + self.suitList[self.suit] + ")"
        elif self.facedown == 0:
            return "********"

    def compare(self, other):
        if self.value > other.value:
            return 1
        if self.value < other.value:
            return -1
        return 0

    def compareSuits(self, other):
        if self.suit == other.suit:
            return 1
        return -1




