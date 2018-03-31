class Table:
	def __init__(self, players):
		self.players = [
			Player(name, Hand()) for name in players]
		self.deck = Deck()
		self.rounds = 0

class Player:
	def __init__(self, name, hand):
		self.name = name
		self.hand = hand

	def give_cards(self, cards):
		self.hand.add_all(cards)

	def drop_cards(self, collection):
		if self.hand.has_cards:
			collection.add_card(self.hand_take_top(), self)

class Hand:
	def __init__(self):
		self.cards = []

	def add_card(self,card):
		self.cards.append(card)

	def take_top(self):
		return self.card.pop(0)

	def add_all(self, cards):
		self.cards.extends(cards)

	def has_cards(self):
		return bool(self.cards)

class Deck:
	def __init__(self):
		self.cards = [
			
		