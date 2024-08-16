from typing import List, Optional


def calculate_comfort_index(
    temperature: int, humidity: float, wind_speed: Optional[float] = None
) -> float:
    result = (100 - humidity) + (30 - temperature)
    if wind_speed is not None:
        result -= wind_speed / 2
    return result


def calculate_traffic_flow_efficiency(
    average_speed: float, traffic_density: List[float], incident_reports: Optional[int] = None
) -> float:
    efficiency = average_speed / (sum(traffic_density) + 1)
    if incident_reports is not None:
        efficiency -= 2 * incident_reports
    return efficiency


def calculate_safety_score(
    road_quality: int,
    lighting_conditions: int,
    accident_history: int,
    average_speed: float,
    traffic_density: List[float],
    incident_reports: Optional[int] = None,
    wind_speed: Optional[float] = None,
) -> float:
    inverse_traffic_density = 1 / sum(traffic_density)
    inverse_accident_history = 1 / (accident_history + 1)
    score = inverse_traffic_density
    score += road_quality * inverse_accident_history
    score += lighting_conditions * average_speed

    if incident_reports is not None:
        score -= incident_reports

    if wind_speed is not None:
        score -= wind_speed
    return score


def calculate_overall_commute_quality_score(
    comfort_index: float, traffic_flow_efficiency: float, safety_score: float
) -> float:
    return (comfort_index + traffic_flow_efficiency + safety_score) / 3
