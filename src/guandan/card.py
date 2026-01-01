from dataclasses import dataclass
from enum import Enum
import functools
from game.utils import enum_ordering


class Suit(str, Enum):
    Spades = "Spades"
    Hearts = "Hearts"
    Clubs = "Clubs"
    Diamonds = "Diamonds"


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

@functools.total_ordering
@dataclass
class Card:
    rank: Rank
    suit: Suit

    def __eq__(self, other: Card):
        return self.rank == other.rank

    def __lt__(self, other: Card):
        return self.rank < other.rank
