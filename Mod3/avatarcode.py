#1: AVATAR AS A CLASS
class Character():
	'''class of Avatar characters'''
			##arguments
	def __init__(self, name, alias, role, abilities):
	'''initialize values'''
			##attributes
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities

from models import Character

chr1 = Character('Aang', 'The Avatar', 'Hero', 'Master of the Elements')

chr2 = Character('Zuko', 'Blue Spirit', 'Hero', 'Lightning Redirection')

chr3 = Character('Azula', 'Crazy Princess', 'Villain', 'Blue Firebending')

chr4 = Character('Ozai', 'Firelord', 'Villain', 'Firebending, Lightning')


class Character_Methods():
	'''class of avatar characters'''
	def __init__(self, name, alias, role, abilities):
		'''initialize values'''
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities
