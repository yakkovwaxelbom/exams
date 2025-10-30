import sys

from game_logic.game import init_game, play_round, winner_with_A_spades, no_winner
from globals.enums import WinnerGame
from utils.accessories import print_win


def main_loop(week_winner, name_p1, name_p2):
    players_and_deck = init_game(name_p1, name_p2)
    p1 = players_and_deck['player_1']
    p2 = players_and_deck['player_2']

    while len(p1['hand']) > 0 and len(p2['hand']) > 0:
        play_round(p1, p2)

    if len(p1['won_pile']) == len(p2['won_pile']):
        win = week_winner(p1, p2)
    else:
        win = WinnerGame.p1.value if len(p1['won_pile']) > len(p2['won_pile']) else WinnerGame.p2.value

    print_win(win, p1, p2)


if __name__ == '__main__':

    func_weak_win = winner_with_A_spades
    name_p1 = None
    name_p2 = None

    if len(sys.argv) > 1:
        func_weak_win = sys.argv[1]
    if len(sys.argv) > 2:
        name_p1 = sys.argv[2]
    if len(sys.argv) > 3:
        name_p2 = sys.argv[3]

    main_loop(func_weak_win, name_p1, name_p2)
# import os, sys
#
# print("Current dir:", os.getcwd())
# print("Sys.path:", sys.path)
# /home/mefathim/כללי/צהל/exams/exams/week_1
# /home/mefathim/כללי/צהל/exams/exams/week_1

# import os, sys
#
# with open('log.txt', 'a') as f:
#     print("CWD:", os.getcwd(), file=f)
#     print("PYTHONPATH:", os.environ.get("PYTHONPATH"), file=f)
#     print("sys.path:", sys.path, file=f)
#     print(file=f)
#     print('-'*15, file=f)
#     print(file=f)

