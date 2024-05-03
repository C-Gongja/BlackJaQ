from random import shuffle

values = list(range(2,15))
suits = ['hearts', 'diamonds', 'clubs', 'spades']

# face_cards = {
# 	11: 'J',
# 	12: 'Q',
# 	13: 'K',
# 	14: 'A',
# 	'J': 11,
# 	'Q': 12,
# 	'K': 13,
# 	'A': 14
# }

class Deck:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		value = self.value
		return f'{value}_of_{self.suit}'
	
def generate_deck():
	deck = []
	for suit in suits:
		for value in values:
			deck.append(Deck(value, suit))
	return deck

def shuffle_deck(deck):
	shuffle(deck)
	return deck

def deal(deck, num_players, num_cards):
	hands = []
	for i in range(num_players):
		hand = []
		for j in range(num_cards):
			hand.append(deck.pop(0))
		hands.append(hand)
	return hands
