class Player(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def playerInfo(self):
        return self.name + "with score of" + self.score + "\n"

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score

    def compScores(self, otherPlayer):
        if self.score > otherPlayer.score:
            return 1
        if self.score < otherPlayer.score:
            return -1
        return 0


