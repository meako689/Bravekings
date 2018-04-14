import random
import string
import os

card_count = 0

os.system('color 0a')

def card_name():
	global card_count
	card_count += 1
	return string.ascii_lowercase[card_count]


class King:
	def __init__(self):
		self.hp = 50

	def __str__(self):
		return "King: HP:{}".format(self.hp)


class Card:

	types = 'Warrior Archer Mage'.split( )
	
	def __init__(self):
		self.hp = random.randint(1, 5)
		self.dmg = random.randint(1, 10)
		self.type = random.choice(self.types)
		self.name = card_name()

	def __str__(self):
		return "Card: {}, HP: {}, DMG: {}, TYPE: {} ".format(self.name, self.hp, self.dmg, self.type) 

	def __repr__(self):
		return self.__str__()

	def attack(self, enemy_card):
		enemy_card.hp = enemy_card.hp - self.dmg
		self.hp = self.hp - enemy_card.dmg

class Player:
	def __init__(self, name, king, cards):
		self.name = name
		self.king = king
		self.hand = cards
		self.table_cards = []

	def take_cards(self):
		self.hand = [ Card(), Card(), Card()]

	def put_cards(self):
		print(self.name, self.king, self.hand)
		while self.hand:
			card_name = input('What card to put?  ')
			table_card = filter(lambda card: card.name == card_name, self.hand).__next__()
			index = self.hand.index(table_card)
			self.hand.pop(index)
			self.table_cards.append(table_card)	
			question = input("That`s all? Y/N: ")
			if question == 'Y':
				break



class Table:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.winner = None

	def battle(self, me, enemy):
		print('/////////////Battle\\\\\\\\\\\\\\')
		print("Table:  ")
		print("Player: {}, {}, Cards: {}".format(me.name, me.king, me.table_cards))
		print("Player: {}, {}, Cards: {}".format(enemy.name, enemy.king, enemy.table_cards))
		print('\\\\\\\\\\\\\\      /////////////')
		for card in me.table_cards:
			battle_quest = input("Choose card which to attack:  ")
			enemy_card = filter(lambda card: card.name == battle_quest, enemy.table_cards).__next__()
			card.attack(enemy_card)
			if enemy_card.hp <= 0:
				enemy.table_cards.pop(enemy.table_cards.index(enemy_card))
			if card.hp <= 0:
				me.table_cards.pop(me.table_cards.index(card))	

class Game:
	def first_round():
		print('First round starts') 
		player1.take_cards()
		player2.take_cards()
		while player1.hand or player2.hand:
			player1.put_cards()
			player2.put_cards()
			while player1.table_cards and player2.table_cards:
				table.battle(player1, player2)
				table.battle(player2, player1)
		if player1.table_cards:
			round_winner = player1
			round_loser = player2
			print("Winner ", round_winner)
			print("Loser ", round_loser)
		else:
			round_winner = player2
			round_loser = player1
			print("Winner ", round_winner)
			print("Loser ", round_loser)
		for card in round_winner.table_cards:
			card.attack(round_loser.enemy_king)

	def second_round():
		print('Second round starts') 
		player1.take_cards()
		player2.take_cards()
		while player1.hand or player2.hand:
			player1.put_cards()
			player2.put_cards()
			while player1.table_cards and player2.table_cards:
				table.battle(player1, player2)
				table.battle(player2, player1)
		if player1.table_cards:
			round_winner = player1
			round_loser = player2
			print("Winner " + round_winner)
			print("Loser " + round_loser)
		else:
			round_winner = player2
			round_loser = player1
			print("Winner " + round_winner)
			print("Loser " + round_loser)
		for card in round_winner.table_cards:
			card.king_attack(round_loser.enemy_king)


player1 = Player(input('Write Player 1 name: '),
			 King(),
			[])
player2 = Player(input('Write Player 2 name: '), 
			King(),
			[])

table = Table(player1, player2)

while not table.winner:
	rounds = 3
	while rounds:
		rounds = rounds - 1
		Game.first_round()
