import random
import GameElements.Card as Card


class Field(object):

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __init__(self,name, list):
        self.name = name
        self.cards = list

    def __getitem__(self, item):
        return self.cards[item]

    def printField(self):
        temp = ""
        for card in self.cards:
            if isinstance(card, Card.Card):
                temp += (card.getCard() + "\n")
        return temp

    def getname(self):
        return self.name

    def getcards(self):
        return self.cards

    def sortByValue(self):
        self.sort(key=int)

    def shuffleField(self, nshuffle):
        nCards = len(self.cards)
        for shuffle in range(nshuffle):
            for i in range(nCards):
                j = random.randrange(i, nCards)
                [self.cards[i], self.cards[j]] = [self.cards[j], self.cards[i]]

    def removeCard(self, card):
        temp = []
        if card in self.cards:
            temp = self.cards.remove(card)
        else:
            return None

    def removeCardIndex(self, index):
        if index >= 0 and index <= len(self):
            return self.cards.pop(index)

    def addCard(self, card):
         self.cards.append(card)

    def addCardIndex(self, index, card):
        if index >= 0 and index <= len(self):
            self.cards.insert(index, card)

    def deckSize(self):
        return len(self.cards)

    def isEmpty(self):
        return len(self.cards) == 0

    def move(self, card, destination):
        temp = []
        for c in self.cards:
            if c == card:
                temp = c;
        self.removeCard(card)
        destination.addCard(temp)

    def draw(self, n, deck):
        for x in range(n):
            self.cards.append(deck.cards.pop())


