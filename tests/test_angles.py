import pytest
import math
from src.analysis.angles import angle




def test_angle_90_degrees():
    assert angle([1, 0], [0, 0], [0, 1]) == pytest.approx(90.0)


def test_angle_180_degrees():
    # points on opposite sides of the vertex, on one line
    assert angle([-1, 0], [0, 0], [1, 0]) == pytest.approx(180.0)


def test_angle_0_degrees():
    # both points on the same side of the vertex
    assert angle([1, 0], [0, 0], [2, 0]) == pytest.approx(0.0, abs=1e-6)


def test_angle_45_degrees():
    assert angle([2, 0], [0, 0], [1, 1]) == pytest.approx(45.0)
