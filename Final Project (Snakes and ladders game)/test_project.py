from project import character, dice, draw_map
import pytest

def test_character():
    assert character("red").strip() == "🟥"
    assert character("blue").strip() == "🟦"
    assert character("green").strip() == "🟩"
    assert character("purple") == None
    assert character("123") == None

def test_dice():
    for _ in range(100):
        result = dice()
        assert 1 <= result <= 6

def test_draw_map_logic():
    pos1, pos2, _ = draw_map("X", 4, "Player1", "Y", 1, "Player2")
    assert pos1 == 10

    pos1, pos2, _ = draw_map("X", 34, "Player1", "Y", 1, "Player2")
    assert pos1 == 28

    pos1, pos2, _ = draw_map("X", 2, "Player1", "Y", 1, "Player2")
    assert pos1 == 2