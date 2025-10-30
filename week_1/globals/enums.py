from enum import Enum


class Rank(Enum):
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13
    JOKER = float('inf')


class Suit(Enum):
    HEARTS = 'H'
    CLUBS = 'C'
    DIAMONDS = 'D'
    SPADES = 'S'


class WinnerRound(Enum):
    p1 = 'p1'
    p2 = 'p2'
    DRAW = 'war'


class WinnerGame(Enum):
    DRAW = 0
    p1 = 1
    p2 = 2
