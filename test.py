import random

player1_name = input('Write Player 1 name: ')
player2_name = input('Write Player 2 name: ')
player1_cards = [Card(), Card(), Card()]
player2_cards = [Card(), Card(), Card()]
player1_king = King()
player2_king = King()
player1 = Player(player1_name, player1_king, player1_cards)
player2 = Player(player2_name, player2_king, player2_cards)
table = Table(player1, player2)

class King:
	def __init__(self):
		self.hp = 50

class Card:

	types = 'warrior archer mage'.split( )
	
	def __init__(self):
		self.hp = random.randint(1, 5)
		self.dmg = random.randint(1, 10)
		self.type = random.choice(types)

class Player:
	def __init__(self, name, king, cards):
		self.name = name
		self.king = king
		self.hand = cards


class Table:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.player1_cards = []
		self.player2_cards = []
		self.winner = None
while not table.winner:
	rounds = 3
	while rounds:
		rounds = rounds - 1
		print('First round starts')
		print(player1)
		cards = input('What card to put?(From 1 to 3):  ')
		if cards == 1:
			question = input('Thats all? Y/N')
			if question == 'Y':
				print(player1_cards[0])
				player1_cards= player1_cards - 1
			else:
				input('What card to put?(From 2 to 3): ')
				if input == 2:
					print(player1_cards[0, 1])
				else:
					print(player1_cards[0, 1, 2])





