from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name, hp, speed, power, rating_armor):
        self._name = name
        self._hp = hp
        self._speed = speed
        self._power = power
        self._rating_armor = rating_armor

    @property
    def speed(self):
        return self._speed

    @property
    def hp(self):
        return self._hp

    @property
    def name(self):
        return self._name

    @property
    def rating_armor(self):
        return self._rating_armor

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def attack(self, attacked, was_damage, dice):
        pass

    def protect(self, power):
        self._hp -= power

    def if_damage(self, speed):
        return self._rating_armor < speed

    def __str__(self):
        return f"name: {self._name}, hp: {self._hp}, shield: {self._rating_armor}"
