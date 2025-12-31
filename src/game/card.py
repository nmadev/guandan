from enum import Enum
from dataclasses import dataclass
from functools import total_ordering


class Suit(str, Enum):
    Spades = "Spades"
    Hearts = "Hearts"
    Clubs = "Clubs"
    Diamonds = "Diamonds"


def enum_ordering(cls):
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return self.value < other.value
        raise ValueError("Cannot compare different types")

    setattr(cls, "__lt__", __lt__)
    return total_ordering(cls)


@enum_ordering
class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@dataclass
class Card:
    rank: Rank
    suit: Suit
