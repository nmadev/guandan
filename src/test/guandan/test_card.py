from game.card import Card, Rank, Suit

def test_rank_comparison():
    assert Rank.Two < Rank.Three
    assert Rank.Two <= Rank.Two
    assert Rank.Two == Rank.Two

def test_card_comparison():
    a = Card(rank=Rank.Three, suit=Suit.Spades)
    b = Card(rank=Rank.Three, suit=Suit.Diamonds)
    c = Card(rank=Rank.Two, suit=Suit.Spades)
    d = Card(rank=Rank.Two, suit=Suit.Hearts)

    assert a == b
    assert a > c
    assert a >= c
    assert c <= d