from week_1.globals.constants import TEXT_WINNER, TEXT_DRAW
from week_1.globals.enums import WinnerGame


def print_win(win: WinnerGame, p1, p2):
    if win == WinnerGame.p1.value:
        print(TEXT_WINNER(p1['name']))
    elif win == WinnerGame.p2.value:
        print(TEXT_WINNER(p2['name']))
    else:
        print(TEXT_DRAW)
