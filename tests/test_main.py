import pytest
import math

def calculate_distance(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def calculate_distances(points):
    return list(map(lambda point: calculate_distance(point), points))

def test_calculate_distance():
    assert calculate_distance((3, 4)) == 5.0

def test_calculate_distances():
    points = [(1, 1), (2, 2), (3, 3)]
    expected_distances = [math.sqrt(2), math.sqrt(8), math.sqrt(18)]
    assert calculate_distances(points) == pytest.approx(expected_distances)

def test_calculate_distances_empty_list():
    points = []
    assert calculate_distances(points) == []

def test_calculate_distances_single_point():
    points = [(0, 0)]
    assert calculate_distances(points) == [0.0]
