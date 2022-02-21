#1: AVATAR AS A CLASS
class Character():
	'''class of Avatar characters'''
	def __init__(self, name, alias, role, abilities):
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities

#AVATAR CHARACTER METHODS
class Character_Methods():
	'''class of avatar characters'''
	def __init__(self, name, alias, role, abilities):
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities

	def getName(self):
		name = self.name
		return name

	def getAlias(self):
		alias = self.alias
		return alias

	def getRole(self):
		role = self.role
		return role

	def getAbility(self):
		ability = self.abilities
		return abilities

	def useAbility(self):
		print(self.alias + 'used their ability ' + self.abilities)


#AVATAR CHARACTER INHERITENCE
class Character_Inherit():
	'''CLASS OF AVATAR CHARACTERS'''
	def __init__(self, name, alias, role, abilities):
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities

	def getName(self):
		name = self.name
		return name

	def getAlias(self):
		alias = self.alias
		return alias

	def getRole(self):
		role = self.role
		return role

	def getAbility(self):
		ability = self.abilities
		return abilities

class Hero(Character_Inherit):
    '''Class of Avatar heros'''

class Villain(Character_Inherit):
    '''class of Avatar villains'''

from models import Hero, Villain

chr1 = Hero('Aang', 'The Avatar', 'Hero', 'Master of the Elements')

chr2 = Hero('Zuko', 'Blue Spirit', 'Hero', 'Lightning Redirection')

chr3 = Villain('Azula', 'Crazy Princess', 'Villain', 'Blue Firebending')

chr4 = Villain('Ozai', 'Firelord', 'Villain', 'Firebending, Lightning')
