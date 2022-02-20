#1: AVATAR AS A CLASS
class Character():
	'''class of Avatar characters'''
	def __init__(self, name, alias, role, abilities):
		self.name = name
		self.alias = alias
		self.role = role
		self.abilities = abilities

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
            return = alias

	def getRole(self):
		role = self.role
		return role

	def getAbilities(self):
		abilities = self.abilities
		return abilities

	def useAbility(self):
		print(self.alias + 'used their ability ' + self.abilities)
