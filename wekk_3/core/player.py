from wekk_3.core.entity import Entity
from wekk_3.globals.conpig import INITIALIZE_HP_PLAYER, INITIALIZE_SPEED_PLAYER, INITIALIZE_POWER_PLAYER, \
    INITIALIZE_RATING_ARMOR_PLAYER, INITIALIZE_PROFESSION_PLAYER, HP_BOOST_CURE, POWER_BOOST_FIGHTER
from wekk_3.globals.enams import Profession


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, INITIALIZE_HP_PLAYER, INITIALIZE_SPEED_PLAYER, INITIALIZE_POWER_PLAYER,
                         INITIALIZE_RATING_ARMOR_PLAYER)

        self._profession = INITIALIZE_PROFESSION_PLAYER

        if self._profession == Profession.CURE:
            self._hp += HP_BOOST_CURE

        elif self._profession == Profession.FIGHTER:
            self._power += POWER_BOOST_FIGHTER

    def speak(self):
        print(f"Monster beware I am the mighty {self._name}")

    def attack(self, attacked, was_damage, dice):
        temp_speed = dice(20) + self._speed
        temp_power = None

        if war := was_damage(temp_speed):
            temp_power = dice(6) + self._speed
            attacked(temp_power)
        return war, temp_speed, temp_power
