from random import randrange

from ..globals.enums import Rank, Suit, WinnerRound
from ..globals.constants import NUM_REPETITIONS


def create_card(rank: Rank, suit: Suit) -> dict:
    return {'rank': rank, 'suite': suit, 'value': rank.value}


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card['value'] > p2_card['value']:
        return WinnerRound.p1.value
    elif p1_card['value'] < p2_card['value']:
        return WinnerRound.p2.value
    return WinnerRound.DRAW.value


def create_deck() -> list[dict]:
    return [create_card(rank, suit) for rank in Rank if rank != Rank.JOKER for suit in Suit]


def shuffle(deck: list[dict]) -> list[dict]:
    for _ in range(NUM_REPETITIONS):
        while (i := randrange(len(deck))) != (j := randrange(len(deck))):
            deck[i], deck[j] = deck[j], deck[i]
    return deck
