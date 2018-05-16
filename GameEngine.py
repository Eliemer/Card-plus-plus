#A GameEngine that will be used to demonstrate a card game in Card++.

from GameElements.Field import Field
from GameElements.Player import Player
from GameElements.Card import Card
from GameElements.TurnOrder import TurnOrder
import random

turns = int(input("Number of turns: "))
player1 = Player("Player 1", 0)
player2 = Player("Player 2", 0)
card1 = Card(2, "Clubs")
card2 = Card(3, "Hearts")
card3 = Card(4, "Diamonds")
card4 = Card(5, "Spades")
card5 = Card(9, "Hearts")
player1hand = Field("Player 1 Hand")
player1hand.addCard(card1)
player2hand = Field("Player 2 Hand")
player2hand.addCard(card2)
cards = [card1, card2, card3, card4, card5]
deck = Field("Deck")

for dcards in cards:
    deck.addCard(cards)
order = TurnOrder()
order.addPlayer(player1)
order.addPlayer(player2)

for x in range(0, turns):
    if not(deck.isEmpty()):
       if (order.getTurnOf(player1)==0):
            player1hand.addCard(deck.draw(1, deck))
            print("Player 1 hand size: " + str(player1hand.deckSize()))
            order.reverseTurnOrder()
       else:
             player2hand.addCard(deck.draw(1, deck))
             print("Player 2 hand size: " + str(player2hand.deckSize()))
             order.reverseTurnOrder()
    else: #Only to be used for the end of the game.
        competingcard1 = player1hand.draw(1, player1hand)
        competingcard2 = player2hand.draw(1, player2hand)
        if competingcard1.compareSuits(competingcard2)>1:
            player1.setScore(50)
        else:
            player2.setScore(50)

player1.setScore(100) #Scores can be changed arbitrarily.
print(player1.getName()+" score: " +str(player1.getScore()))
print(player2.getName()+" score: " +str(player2.getScore()))