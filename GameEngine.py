#A GameEngine that will be used to demonstrate a card game in Card++.

from GameElements.Field import Field
from GameElements.Player import Player
from GameElements.Card import Card
import random

turns = int(input("Number of turns: "))
player1 = Player("Player 1", 0)
player2 = Player("Player 2", 0)
card1 = Card(2, "Clubs")
card2 = Card(3, "Hearts")
player1hand = Field("Player 1 Hand")
player1hand.addCard(card1)
player2hand = Field("Player 2 Hand")
player2hand.addCard(card2)
for x in range(0, turns):
    #Add required actions
    pass


