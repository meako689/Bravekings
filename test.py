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
		self.dmg = 0

	def __str__(self):
		return "King: HP:{}".format(self.hp)

class KingIsDead(Exception):
	pass

class Card:

	types = 'Warrior Archer Mage'.split( )
	
	def __init__(self):
#		self.hp = random.randint(1, 5)
		self.hp = 5 
		self.dmg = random.randint(1, 10)
		self.type = random.choice(self.types)
		self.name = card_name()

	def __str__(self):
		return "\nCard: {}\t HP: {}\t DMG: {}\t TYPE: {} ".format(self.name, self.hp, self.dmg, self.type) 

	def __repr__(self):
		return self.__str__()

	def attack(self, enemy_card):
		enemy_card.hp = enemy_card.hp - self.dmg
		self.hp = self.hp - enemy_card.dmg
		print("Card HP: {}, Enemy Card HP: {}".format(self.hp, enemy_card.hp))


class Player:
	def __init__(self, name, king, cards):
		self.name = name
		self.king = king
		self.hand = cards
		self.table_cards = []

	def take_cards(self):
		self.hand = [ Card(), Card(), Card()]

	def find_card_by_name(self, name, where):
		return next(filter(lambda card: card.name == name, where), None)

	def put_cards(self):
		print(self.name, self.king, self.hand)
		while self.hand:
			card_name = input('What card to put?  ')
			table_card = self.find_card_by_name(card_name, self.hand)
			if not table_card:
				continue
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

	def battle(self, me, enemy, attack_king=False):
		if not me.table_cards or not enemy.table_cards: 
			return
		print('/////////////Battle\\\\\\\\\\\\\\')
		print("Table:  ")
		print("Player: {}, {}, Cards: {}".format(me.name, me.king, me.table_cards))
		print("Player: {}, {}, Cards: {}".format(enemy.name, enemy.king, enemy.table_cards))
		print('\\\\\\\\\\\\\\      /////////////')
		for card in me.table_cards:
			if attack_king:
				print("You can type 'king' to attack king!")
			battle_quest = input("Player {}: Attack Card {}, Choose card which to attack:  ".format(me.name, card.name))
			if attack_king and battle_quest == 'king':
				card.attack(enemy.king)
				if enemy.king.hp <=0:
					raise KingIsDead()
				return
		
			enemy_card = enemy.find_card_by_name(battle_quest, enemy.table_cards)
			if not enemy_card:
				print ("No such card, go fuck yourself")
				return

			card.attack(enemy_card)
			if enemy_card.hp <= 0:
				enemy.table_cards.pop(enemy.table_cards.index(enemy_card))
		import pdb; pdb.set_trace()
		me.table_cards = list(
			filter(lambda c: c.hp > 0, me.table_cards)) # remove dead cards


	
	def has_winner(self):
		if player1.king.hp <=0:
			self.winner = player2
			self.loser = player1
		elif player2.king.hp <=0:
			self.winner = player1
			self.loser = player2
		if self.winner:
			return True

class Game:
	def play_round(round, attack_king=False):
		print('Round {} start'.format(round)) 
		player1.take_cards()
		player2.take_cards()

		while player1.hand or player2.hand:
			player1.put_cards()
			player2.put_cards()
			while player1.table_cards and player2.table_cards:
				table.battle(player1, player2, attack_king)
				table.battle(player2, player1, attack_king)
			if player1.table_cards:
				round_winner = player1
				round_loser = player2
			elif player2.table_cards:
				round_winner = player2
				round_loser = player1
			else:
				print('Draw!')
				return

			print("Winner Player {} ".format(round_winner.name))
			print("Loser Player {}".format(round_loser.name))
			for card in round_winner.table_cards:
				print("{} king {} damaged".format(round_loser.name, card.dmg))
				card.attack(round_loser.king)



player1 = Player(input('Write Player 1 name: '),
			 King(),
			[])
player2 = Player(input('Write Player 2 name: '), 
			King(),
			[])

table = Table(player1, player2)

while not table.winner:
	rounds = 1
	while rounds < 4:
		attack_king = rounds == 3
		try:
			Game.play_round(rounds, attack_king)
		except(KingIsDead):
			pass
		rounds = rounds + 1

		if table.has_winner():
			break
print("Winner {}".format(table.winner.name))