from ..src.rle_decode import RLEDecoder


def test_rle_decode_1():
    expected = "AABBBCCCC"
    data = "A2B3C4"
    response = RLEDecoder(data)
    assert expected == str(response)
    assert expected.count("B") == response.count("B")
    assert len(expected) == len(response)


def test_rle_decode_2():
    expected = "AABBBCCCC" * 10
    data = "A2B3C4" * 10
    response = RLEDecoder(data)
    assert expected == str(response)
    assert expected.count("A") == response.count("A")
    assert len(expected) == len(response)


def test_rle_decode_3():
    expected = "AABBXXXXBCPPC"
    data = "A2B2X4B1C1P2C1"
    response = RLEDecoder(data)
    assert expected == str(response)
    assert expected.count("X") == response.count("X")
    assert len(expected) == len(response)


def test_rle_decode_4():
    expected = "AABBBCCCC" * 2
    data = "A2B3C4" * 2
    response = RLEDecoder(data)
    assert expected == str(response)
    assert expected.count("C") == response.count("C")
    assert len(expected) == len(response)


def test_rle_decode_5():
    expected = "AABBBCDDDDFFWWWW"
    data = "A2B3C1D4F2W4"
    response = RLEDecoder(data)
    assert expected == str(response)
    assert expected.count("W") == response.count("W")
    assert len(expected) == len(response)
