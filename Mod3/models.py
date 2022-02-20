##1: AVATAR AS A CLASS
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

class Character_Methods():
	'''class of avatar characters'''
	def__init__(self, name, alias, role, abilities):
		'''initialize values'''
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities
#functions below are methods vvv
	def getName(self):
		name = self.name
		return name

	def getAbilities(self):
		abilities = self.abilities
		return abilities

	def useAbility(self):
		print(self.alias + 'used their ability ' + self.abilities)
