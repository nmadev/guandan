from game.card import Card, Rank, Suit

def test_rank_comparison():
    assert Rank.Two < Rank.Three
    assert Rank.Two <= Rank.Two
    assert Rank.Two == Rank.Two