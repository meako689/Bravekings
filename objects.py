import random

class Table:
	def __init__(self, players):
		self.players = [
			Player(name, Hand()) for name in players]
		self.deck = Deck()
		self.rounds = 0
	def deal_cards(self):
        self.deck.shuffle()
        self.deck.setup_hands(self.players)
        for player in self.players:
            player.show_hand()
    def count_round(self):
        self.rounds += 1
        print_underline('Starting round {}'.format(self.rounds), '=')
    def play_all(self):
        while not self.finished:
            self.play_once()
        self.show_winner()
    def show_winner(self):
        for player in self.players:
            if player.hand.has_cards:
                print()
                print(player.name, 'wins!')
                break
    def finished(self):
        return sum(bool(player.hand.cards) for player in self.players) == 1

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
		cards = int(80)
	def create_deck(cards):
		

class Card:
	def __init__(self):
		hp = int()
		damage = int()
		type = [ warrior, archer, mage]

class King:
	def __init__(self):
		king = True
		hp = int(50)

class Game:
	def main():
		table = Table([ player1, player2])
		player1 = str(input("Write your name:"))
		player2 = str(input("Write your name:"))
		table.deal_cards()
		table.play_all()

main()