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
        if isinstance(other, type(self)):
            return self.value < other.value
        raise ValueError("Cannot compare different types")

    setattr(cls, "__lt__", __lt__)
    return total_ordering(cls)


@enum_ordering
class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


@dataclass
class Card:
    rank: Rank
    suit: Suit
