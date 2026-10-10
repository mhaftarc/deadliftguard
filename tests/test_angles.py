import pytest
import math
from src.analysis.angles import angle, trunk_angle




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

def test_trunk_angle_vertical():
    # shoulder directly above hip
    assert trunk_angle([0, 0], [0, -1]) == pytest.approx(0.0, abs=1e-6)


def test_trunk_angle_horizontal():
    assert trunk_angle([0, 0], [1, 0]) == pytest.approx(90.0)


def test_trunk_angle_45_degrees():
    assert trunk_angle([0, 0], [1, -1]) == pytest.approx(45.0)


def test_trunk_angle_unsigned_left_and_right():
    # leaning left and right gives the same angle (unsigned by design)
    left = trunk_angle([0, 0], [-1, -1])
    right = trunk_angle([0, 0], [1, -1])
    assert left == pytest.approx(right)