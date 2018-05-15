import random


class Field(object):

    def __init__(self, name):
        self.name = name
        self.cards = []

    def printField(self):
        for card in self.cards:
            card.printCard()

    def sortByValue(self):
        self.sort(key=int)

    def shuffleField(self, nshuffle):
        nCards = len(self.cards)
        for shuffle in range(nshuffle):
            for i in range(nCards):
                j = random.randrange(i, nCards)
                [self.cards[i], self.cards[j]] = [self.cards[j], self.cards[i]]

    def removeCard(self, card):
        if card in self.cards:
            return self.cards.remove(card)
        else:
            return

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
        temp = self.cards[card]
        destination.append(temp)
        self.removeCard(card)

    def draw(self, n, deck):
        temp = deck.cards.pop(n)
        self.cards.append(temp)


