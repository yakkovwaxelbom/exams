from enum import Enum


class Profession(Enum):
    CURE = 0
    FIGHTER = 1


class MonsterType(Enum):
    ORC = 0
    GOBLIN = 1


class Weapon(Enum):
    KNIFE = 0
    SWORD = 1
    AX = 2


class WeaponDamage(Enum):
    KNIFE = 0.5
    SWORD = 1
    AX = 1.5


class StatusGame(Enum):
    PLAYER_WIN = 0
    MONSTER_WIN = 1
    RUN = 3
