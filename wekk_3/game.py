from random import choice, randint
from faker import Faker

from wekk_3.core.goblin import Goblin
from wekk_3.core.orc import Orc
from wekk_3.core.player import Player
from wekk_3.globals.enams import MonsterType, StatusGame


class Game:

    def __init__(self):
        self.__monster = self.__monster_random_choose()
        self.__player = self.__player_create()
        self.__players_pool = self.__get_who_first()
        self.__status = StatusGame.RUN

    def __player_create(self):
        name = Faker().name()
        return Player(name)

    def __monster_random_choose(self):
        monster = None
        name = Faker().name()
        _type = choice(list(MonsterType))

        if _type == MonsterType.ORC:
            monster = Orc(name)
        elif _type == MonsterType.GOBLIN:
            monster = Goblin(name)

        return monster

    def dice_roll(self, sides):
        return randint(1, sides)

    def __get_who_first(self):
        score_ply = self.__player.speed + self.dice_roll(6)
        score_mon = self.__monster.speed + self.dice_roll(6)
        return [self.__player, self.__monster] if score_ply >= score_mon else [self.__monster, self.__player]

    def __change_turn(self):
        return self.__player if self.__players_pool is self.__player else self.__monster

    def __check_status(self):
        if self.__player.hp <= 0:
            self.__status = StatusGame.MONSTER_WIN
        elif self.__monster.hp <= 0:
            self.__status = StatusGame.PLAYER_WIN

    def __loop_game(self):
        while self.__status == StatusGame.RUN:
            details = self.__players_pool[0].attack(self.__players_pool[1].protect, self.__players_pool[1].if_damage,
                                                    self.dice_roll)
            self.__check_status()
            self.__players_pool[0], self.__players_pool[1] = self.__players_pool[1], self.__players_pool[0]
            self.print_status_turn(details)

    def __menu_show(self):
        while (user_input := input('To approach, press b, to exit, press e.\n')) not in ['b', 'e']:
            print('invalid input')

        if user_input == 'b':
            print('The competitors:')
            self.__player.speak()
            self.__monster.speak()
            print()

            return True
        return False

    def print_status_turn(self, details):
        print(f'{self.__players_pool[0].name} fighting with {self.__players_pool[1].name}')
        print(f'power: {details[1]} vs shield: {self.__players_pool[1].rating_armor}')

        if details[0]:

            print(f"There was a victory worth {details[1]} hp")
        else:
            print('There was no battle.')

        print(self.__player)
        print(self.__monster)
        print('\n' + '-' * 20)

    def print_end_game(self):
        if self.__status == StatusGame.PLAYER_WIN:
            name_win = self.__player.name
        else:
            name_win = self.__monster.name

        print(f"{name_win} win")

    def start(self):
        if self.__menu_show():
            self.__loop_game()
            self.print_end_game()
