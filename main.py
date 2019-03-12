import random
import copy

global_deck = [ (2,1),(2,2),(2,3),(2,4),
		 (3,1),(3,2),(3,3),(3,4),
		 (4,1),(4,2),(4,3),(4,4),
		 (5,1),(5,2),(5,3),(5,4),
		 (6,1),(6,2),(6,3),(6,4),
		 (7,1),(7,2),(7,3),(7,4),
		 (8,1),(8,2),(8,3),(8,4),
		 (9,1),(9,2),(9,3),(9,4),
		 (10,1),(10,2),(10,3),(10,4),
		 (11,1),(11,2),(11,3),(11,4),
		 (12,1),(12,2),(12,3),(12,4),
		 (13,1),(13,2),(13,3),(13,4),
		 (14,1),(14,2),(14,3),(14,4)]

### 1 -- Spades
### 2 -- Hearts
### 3 -- Clubs
### 4 -- Diamonds

def remove(card,deck):
	deck.remove(card)

def add(card,deck):
	deck.append(card)

def draw(number, deck_):
	result_ = []
	for n in range(number):
		card = random.choice(deck_)
		remove(card, deck_)
		add(card, result_)

	return(tuple(result_))


class table:
	def __init__(self, players, board, deck, pot):
		self.players = players #array of tuples: (id)
		"""
		player = [(card1, card2), balance, id]
		board = [card1,card2,card3,card4,card5]
		deck = [(card1, ... , card52)]
		pot = n #value in points
		"""

		self.board = board
		self.deck = deck
		self.pot = pot
		"""
		[(card1, card2, card3, card4, card5), pot, turn)]
		-> Turn pays big blind, turn + 1 pays small blind
		"""

	def deal(self):
		for player in self.players:
			player[0] = draw(2, self.deck)

	def flip(self):
		self.board += draw(1, self.deck)

	def shuffle(self):
		self.deck = copy.copy(global_deck)
		self.board = []
		for player in self.players:
			player[0] = 0

def test_draw():
	deck_ = copy.copy(global_deck)
	test = draw(52, deck_)
	
	print(deck_)
	print(test)

	for element in test:
		print(element in deck_) 

def test_table():
	a = table([[(), 100, 1],[(), 100, 2],[(), 100, 3]],[],copy.copy(global_deck),0)
	a.deal()
	print(a.players)
	print()
	a.flip()
	a.flip()
	a.flip()
	print(a.board)
	print(len(a.deck))
	a.shuffle()
	print()
	print(a.board)
	print(a.players)
	print(len(a.deck))


def main():
	#test_draw()
	test_table()
	pass

if __name__ == "__main__":
	main()




