class Card(object):

    def __init__(self, value, suit):
        suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
        valueList = {
            "Ace": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13
        }


        if eval(suit) in suitList and eval(value) in valueList:
            self.suit = eval(suit)
            self.value = valueList[eval(value)]
            self.facedown = False

    def flip(self):
        self.facedown = not self.facedown
        return self.facedown

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

    def getCard(self):
        if not self.facedown:
            return str(self.getValue()) + " of " + self.getSuit()
        else:
            return "***"

    def compareValue(self, other):
        if self.value > other.value:
            return 1
        elif self.value < other.value:
            return -1
        else:
            return 0

    def compareSuits(self, other):
        if self.suit == other.suit:
            return 1
        return -1

    def getCardAnyway(self):
        return str(self.value) + " of " + self.suit



