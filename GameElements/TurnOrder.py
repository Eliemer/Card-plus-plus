class TurnOrder:

    def __init__(self):
        self.turnOrder = []

    def addPlayer(self, player):
        self.turnOrder.append(player)

    def removePlayer(self, player):
        self.turnOrder.remove(player)

    def getTurnOf(self, player):
        return self.turnOrder.index(player)

    def getPlayer(self, index):
        return self.turnOrder[index]

    def moveTurnOrder(self, player1, player2):
        i, j = self.turnOrder.index(player1), self.turnOrder.index(player2)
        self.turnOrder[j], self.turnOrder[i] = self.turnOrder[i], self.turnOrder[j]

    def reverseTurnOrder(self):
        return self.turnOrder.reverse()
