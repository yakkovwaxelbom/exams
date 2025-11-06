from random import randint, choice

from wekk_3.globals.enams import Profession, Weapon

# Player initialization
INITIALIZE_HP_PLAYER = 50
INITIALIZE_SPEED_PLAYER = randint(5, 10)
INITIALIZE_POWER_PLAYER = randint(5, 10)
INITIALIZE_RATING_ARMOR_PLAYER = randint(5, 15)
INITIALIZE_PROFESSION_PLAYER = choice(list(Profession))
HP_BOOST_CURE = 10
POWER_BOOST_FIGHTER = 2

# Monster initialization
INITIALIZE_WEAPON_MONSTER = choice(list(Weapon))

# Orc initialization
INITIALIZE_HP_ORC = 50
INITIALIZE_SPEED_ORC = randint(5, 10)
INITIALIZE_POWER_ORC = randint(5, 15)
INITIALIZE_RATING_ARMOR_ORC = randint(2, 8)

# Goblin initialization
INITIALIZE_HP_GOBLIN = 50
INITIALIZE_SPEED_GOBLIN = randint(5, 10)
INITIALIZE_POWER_GOBLIN = randint(5, 10)
INITIALIZE_RATING_ARMOR_GOBLIN = 1
CHANCE_OF_ESCAPE = 0.3
