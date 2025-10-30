from random import randint

from week_2.globals.enums import Rank, Suit
from week_2.globals.constants import NUM_SWAPS_SHUFFLE


def build_standard_deck() -> list[dict]:
    return [{'rank': rank, 'suite': suit} for rank in Rank for suit in Suit]


def shuffle_by_suit(deck: list[dict], swaps: int = NUM_SWAPS_SHUFFLE) -> list[dict]:
    for _ in range(swaps):
        flag_while = True

        i = randint(0, len(deck) - 1)
        j = None

        while flag_while:
            j = randint(0, len(deck) - 1)
            if deck[j]['suite'] == Suit.HEARTS and j % 5 == 0:
                flag_while = False
            elif deck[j]['suite'] == Suit.CLUBS and j % 3 == 0:
                flag_while = False
            elif deck[j]['suite'] == Suit.DIAMONDS and j % 2 == 0:
                flag_while = False
            elif deck[j]['suite'] == Suit.SPADES and j % 7 == 0:
                flag_while = False

        deck[i], deck[j] = deck[j], deck[i]

    return deck
