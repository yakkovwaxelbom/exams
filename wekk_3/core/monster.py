from abc import abstractmethod

from wekk_3.core.entity import Entity
from wekk_3.globals.conpig import INITIALIZE_WEAPON_MONSTER
from wekk_3.globals.enams import Weapon


class Monster(Entity):
    weapon_damage = {
        Weapon.KNIFE: 0.5, Weapon.SWORD: 1, Weapon.AX: 1.5
    }

    def __init__(self, name, hp, speed, power, rating_armor, _type):
        super().__init__(name, hp, speed, power, rating_armor)
        self._type = _type
        self._weapon = INITIALIZE_WEAPON_MONSTER

    def speak(self):
        print(
            f'The {self._type.name.lower()} {self._name} The most lovely and beautiful of all the lovely and beautiful')

    def attack(self, attacked, was_damage, dice):

        temp_speed = dice(20) + self._speed
        temp_power = None

        if war := was_damage(temp_speed):
            temp_power = Monster.weapon_damage[self._weapon] * (dice(6) + self._speed)
            attacked(temp_power)
        return war, temp_speed, temp_power
