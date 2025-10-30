from enum import Enum


class Rank(Enum):
    ACE = 1
    TWO = 2
    # THREE = 3
    # FOUR = 4
    # FIVE = 5
    # SIX = 6
    # SEVEN = 7
    # EIGHT = 8
    # NINE = 9
    # TEN = 10
    # JACK = 10
    # QUEEN = 10
    # KING = 10


class Suit(Enum):
    HEARTS = 'H'
    CLUBS = 'C'
    DIAMONDS = 'D'
    SPADES = 'S'


class StatusGame(Enum):
    PLAYER_TURN = 0
    DEALER_TURN = 1
    PLAYER_LOOS = 2
    DEALER_LOOS = 3
    CARD_DISCOVERY = 4
    DRAW = 5
