# Card ++

**Introduction**

A card game is any game that uses cards as the primary
device with which the game is played. 
Card games have always been a big part of human history.
As such, we want to give people a tool to be able to 
continue this tradition via computer programs.


As part of our Structure and Properties of Programming 
Languages course we have been tasked with the creation 
of a new programming language which, in our case, would result
in being able to create card games in a short amount of 
time, with little experience in programming required.

We want to create a language that would facilitate the
development of any card game imaginable.
For the scope of this project we will 
limit Card++ to only be able to use
the fifty-two casino suite cards.

**Tutorial**

Below is a video verison of the Card++ tutorial. Make sure that you turn on the Closed Captions.

[![Card++ Tutorial](https://img.youtube.com/vi/yCm0ClWMNVQ/1.jpg)](https://www.youtube.com/watch?v=yCm0ClWMNVQ "Card++ Tutorial")



**Tools Used**

PLY - PLY (Python Lex-Yacc) is an implementation
of lex and yacc parsing tools for
Python, developed by David Beazley. This tool is used to 
establish and interpret our language's grammar.

**Installation**

1. Download Card++ from our GitHub
repository at _https://github.com/Eliemer/Card-plus-plus .
2. Make sure that you have Python 3 (3.6) 
installed in your machine with the PLY (3.10) library.
3. Run the _Card++.py_ file on your IDE or terminal.
4. Start using Card++.

**Language Developement**

The programming language was created utilizing python; the lexical
analyzer itself along with some intermediate code are contained in 
Card++.py. The data structures used are in the GameElements File, which 
allows our Language to create objects such as Cards, Fields, etc.

Initial development consisted of choosing keywords for users to utilize
in the Language, creating those keywords and then building expressions 
and functions as needed to allow them to build objects quickly and easily.
It was assured then that all the functions a user would write could be 
interpreted and defined in the Language to create the Cards and Fields 
and then combined to be utilized in the Card game itself along with
other functions to affect the Fields and Cards themselves.


**Card++ Reference Manual**

Card++ allows you to create your card game using the
fifty-two casino suit cards. 


Cards:

A simple declaration to start creating the cards in the game.

- Card _cardname_ = ("_value_","_suit_");
 
For example, if we want to declare the three of
diamonds, we would type the following in Card++:

Card Diamonds3 = ("3", "Diamonds");

A valid card declaration receives a valid value and suit 
as parameters, though we can declare the name however we want.


Fields: 

After you declare the desired number of cards, a field can be
created to represent the different types of fields in a card
game. The following is the syntax used to declare a field:

Field _fieldname_ [_Card 0, Card 1, Card 2, ... , Card N-1_];

We could declare a Field composed of only the three of 
diamonds:

Field Deck [Diamonds3];

It is also valid to declare an empty field, for example
an empty hand would be declared as follows:

Field Hand [];

After the hands and fields are declared, it is valid to 
operate on them using Card++'s functions.

Some functions are:

Shuffle(Deck);

- Shuffles a field to randomize their order in any given field, whether
it's a deck, a player's hand or any other pile.

flip (Diamonds3);

- Toggles visibility of a card in any given field, to allow certain cards
to be able to be viewed by a player or not, such as another player's hand,
a card being face-down on the playing field, or simply making the deck
invisible to players.

Draw(Deck);

- Draws the top card from the given Field and adds it to the player's hand.


**Developers**

This project was developed by Eliemer Velez, Ariel Torres
and Jonathan Irizarry under the supervision of Dr. Wilson
Rivera at the University of Puerto Rico - Mayaguez Campus.




