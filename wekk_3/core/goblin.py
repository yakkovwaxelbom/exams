from random import random

from wekk_3.core.monster import Monster
from wekk_3.globals.conpig import INITIALIZE_HP_GOBLIN, INITIALIZE_SPEED_GOBLIN, INITIALIZE_POWER_GOBLIN, \
    INITIALIZE_RATING_ARMOR_GOBLIN, CHANCE_OF_ESCAPE
from wekk_3.globals.enams import MonsterType


class Goblin(Monster):
    def __init__(self, name):
        super().__init__(name=name,
                         hp=INITIALIZE_HP_GOBLIN,
                         speed=INITIALIZE_SPEED_GOBLIN,
                         power=INITIALIZE_POWER_GOBLIN,
                         rating_armor=INITIALIZE_RATING_ARMOR_GOBLIN,
                         _type=MonsterType.GOBLIN)

    def if_damage(self, speed):
        return self._rating_armor < speed or ((self._hp < INITIALIZE_HP_GOBLIN / 2) and random() < CHANCE_OF_ESCAPE)

    def away_run(self):
        pass
