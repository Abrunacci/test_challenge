from ..src.laxative_shot_roulette import get_chance


def test_laxative_shot_roulette():
        assert get_chance(2, 1, 1) == 0.5
        assert get_chance(4, 1, 3) == 0.25
        assert get_chance(100, 10, 10) == 0.33
        assert get_chance(1000, 150, 20) == 0.04
        assert get_chance(25, 5, 5) == 0.29
        assert get_chance(9, 3, 2) == 0.42
