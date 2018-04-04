import random



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

	def __str__(self):
		return "Card: HP: {}, DMG: {}, TYPE: {}".format(self.hp, self.dmg, self.type) 

	def __repr__(self):
		return self.__str__()

	def attack(self, enemy_card):
		enemy_card.hp = enemy_card.hp - self.dmg 

class Player:
	def __init__(self, name, king, cards):
		self.name = name
		self.king = king
		self.hand = cards
		self.table_cards = []

	def take_cards(self):
		self.hand = [Card(), Card(), Card()]

	def put_cards(self):
		print(self.name, self.king, self.hand)
		while self.hand:
			card_indx = int(input('What card to put?(From 1 to 3):  ')) - 1
			table_card = self.hand.pop(card_indx)
			self.table_cards.append(table_card)	
			question = input("That`s all? Y/N")
			if question == 'Y':
				break



class Table:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.winner = None

	def battle(self, me, enemy):
		print("Table:  ")
		print("Player: {}, Cards: {}".format(me.name, me.table_cards))
		print("Player: {}, Cards: {}".format(enemy.name, enemy.table_cards))
		for card in me.table_cards:
			battle_quest = int(input("Choose card which to attack:  ")) - 1
			enemy_card = enemy.table_cards[battle_quest]
			card.attack(enemy_card)
			if enemy_card.hp <= 0:
				enemy.table_cards.pop(battle_quest)




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
		else:
			round_winner = player2
			round_loser = player1
		for card in round_winner.table_cards:
			card.attack(round_loser.enemy_card)

