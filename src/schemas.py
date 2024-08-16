from enum import Enum

from pydantic import BaseModel, model_validator


class WeatherInput(BaseModel):
    temperature: int
    humidity: float
    wind_speed: float | None = None


class TrafficFlowInput(BaseModel):
    average_speed: float
    traffic_density: list[float]
    incident_reports: int | None = None


class RoadConditionInput(BaseModel):
    road_quality: int
    lighting_conditions: int
    accident_history: int


class CommuteQualityInput(BaseModel):
    weather: WeatherInput
    traffic_flow: TrafficFlowInput
    road_condition: RoadConditionInput


class CommuteQualityParams(BaseModel):
    comfort_index: float
    traffic_flow_efficiency: float
    safety_score: float


class QualityCategoryEnum(Enum):
    POOR = "Poor"
    AVERAGE = "Average"
    GOOD = "Good"


class OverallCommuteQualitySchema(BaseModel):
    quality_score: float
    commute_quality: QualityCategoryEnum | None = None

    @model_validator(mode="before")
    @classmethod
    def set_commute_quality(cls, data: dict) -> dict:
        score = data.get("quality_score")
        if score is None:
            raise ValueError("quality_score is required to determine `commute_quality`")

        commute_quality = data.get("commute_quality")
        if commute_quality is None:
            if score >= 50:
                data["commute_quality"] = QualityCategoryEnum.GOOD
            elif score >= 0:
                data["commute_quality"] = QualityCategoryEnum.AVERAGE
            else:
                data["commute_quality"] = QualityCategoryEnum.POOR
        return data
