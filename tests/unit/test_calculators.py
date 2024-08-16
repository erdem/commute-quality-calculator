from src.calculators import (
    calculate_comfort_index,
    calculate_traffic_flow_efficiency,
    calculate_safety_score,
    calculate_overall_commute_quality_score,
)


def test_calculate_comfort_index():
    assert calculate_comfort_index(25, 60) == 45
    assert calculate_comfort_index(30, 70, 10) == 25
    assert calculate_comfort_index(20, 50, 5) == 57.5


def test_calculate_traffic_flow_efficiency():
    assert calculate_traffic_flow_efficiency(60, [0.5, 0.3, 0.2]) == 30.0
    assert calculate_traffic_flow_efficiency(50, [0.4, 0.4, 0.2], 2) == 21
    assert calculate_traffic_flow_efficiency(40, [0.1, 0.1], 0) == 33.333333333333336


def test_calculate_safety_score():
    assert calculate_safety_score(8, 7, 2, 50, [0.3, 0.4, 0.3]) == 353.6666666666667
    assert calculate_safety_score(9, 8, 1, 60, [0.2, 0.2, 0.1], 3, 5) == 478.5
    assert calculate_safety_score(7, 6, 3, 40, [0.5, 0.5], 1) == 241.75


def test_calculate_overall_commute_quality_score():
    assert calculate_overall_commute_quality_score(45, 60, 120) == 75
    assert calculate_overall_commute_quality_score(25, 21, 472) == 172.66666666666666
