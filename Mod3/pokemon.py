#pokemon as a class
class Pokemon():
	'''class of pokemon characters'''
	def __init__(self, name, type, pokedex, abilities):
		self.name = name
		self.type = type
		self.pokedex = pokedex
		self.abilities = abilities

#pokemon METHODS
class Pokemon_Methods():
    '''class of pokemon characters'''
    def __init__(self, name, type, pokedex, abilities):
        self.name = name
        self.type = type
        self.pokedex = pokedex
        self.abilities = abilities

    def getName(self):
        name = self.name
        return name

    def getType(self):
        type = self.type
        return type

    def getPokedex(self):
        pokedex = self.pokedex
        return pokedex

    def getAbility(self):
		ability = self.abilities
		return abilities

    def useAbility(self):
        print(self.name + ' used ' + self.abilities + '!')

    def pkeFight(self):
        print(self.name + ' made a critical hit!')

    def useAbility(self):
        print(self.name + ' used ' + self.abilities + '! It was super effective!')

#POKEMON INHERITENCE
class Pokemon_Inherit():
    '''class of pokemon'''
    def __init__(self, name, type, pokedex, abilities):
        self.name = name
        self.type = type
        self.pokedex = pokedex
        self.abilities = abilities

    def getName(self):
        name = self.name
        return name

    def getType(self):
        type = self.type
        return type

    def getPokedex(self):
        pokedex = self.pokedex
        return pokedex

    def getAbility(self):
        ability = self.abilities
        return abilities

class Male(Pokemon_Inherit):
    '''class of male pokemon'''
    def showOff(self):
        print(self.name + ' showed off his coolest pose!')

class Female(Pokemon_Inherit):
    '''class of female pokemon'''
    def doFlirt(self):
        print(self.name + ' did a cute pose!')

from pokemon import Male, Female

pke1 = Male('Charizard', 'Fire, Flying', '#006', 'Blaze')

pke2 = Male('Poliwrath', 'Water, Fighting', '#062', 'Water Absorb')

pke3 = Female('Electabuzz', 'Electric', '#125', 'Static')

pke4 = Female('Gengar', 'Ghost, Poison', '#94', 'Cursed Body')
