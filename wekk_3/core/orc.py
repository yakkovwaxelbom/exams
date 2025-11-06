from wekk_3.core.monster import Monster
from wekk_3.globals.conpig import INITIALIZE_HP_ORC, INITIALIZE_SPEED_ORC, INITIALIZE_POWER_ORC, \
    INITIALIZE_RATING_ARMOR_ORC
from wekk_3.globals.enams import MonsterType


class Orc(Monster):
    def __init__(self, name):
        super().__init__(name=name,
                         hp=INITIALIZE_HP_ORC,
                         speed=INITIALIZE_SPEED_ORC,
                         power=INITIALIZE_POWER_ORC,
                         rating_armor=INITIALIZE_RATING_ARMOR_ORC,
                         _type=MonsterType.GOBLIN)

