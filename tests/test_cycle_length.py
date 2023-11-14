from ..src.cycle_length import cycle_length


def test_cycle_length():
    assert cycle_length([2, 0, 1, 4, 3, 5], 0) == 3
    assert cycle_length([7, 3, 5], 0) == -1
    assert cycle_length([2, 0, 4, 2, 3, 5], 4) == 3
    assert cycle_length([2, 6, 4, 2, 1, 5, 3], 1) == 5
    assert cycle_length([2, 7, 4, 1, 3, 5, 2], 5) == 1
    assert cycle_length([2, 6, 4, 2, 3, 5, 8], 6) == -1
