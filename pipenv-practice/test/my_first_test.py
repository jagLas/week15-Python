import pytest
from polygon import RegularPolygon


def test_squares_perimeter():
    s = RegularPolygon(4, 5)
    assert RegularPolygon.get_perimeter(s) == 20