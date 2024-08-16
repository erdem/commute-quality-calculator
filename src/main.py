import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

from pydantic import ValidationError

import calculators
from schemas import (
    CommuteQualityInput,
    CommuteQualityParams,
    OverallCommuteQualitySchema,
)


def load_json(json_string: str) -> Dict[Any, Any]:
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON Input: {e}")


def load_json_file(file_path: str) -> Dict[Any, Any]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    with path.open("r") as f:
        return load_json(f.read())


def get_commute_quality(input_data: Dict[Any, Any]) -> OverallCommuteQualitySchema:
    try:
        cq_input = CommuteQualityInput(**input_data)
    except ValidationError as e:
        raise ValueError(f"Invalid input data: {e}")

    comfort_index = calculators.calculate_comfort_index(
        temperature=cq_input.weather.temperature,
        humidity=cq_input.weather.humidity,
        wind_speed=cq_input.weather.wind_speed,
    )
    traffic_flow_efficiency = calculators.calculate_traffic_flow_efficiency(
        average_speed=cq_input.traffic_flow.average_speed,
        traffic_density=cq_input.traffic_flow.traffic_density,
        incident_reports=cq_input.traffic_flow.incident_reports,
    )
    safety_score = calculators.calculate_safety_score(
        road_quality=cq_input.road_condition.road_quality,
        lighting_conditions=cq_input.road_condition.lighting_conditions,
        accident_history=cq_input.road_condition.accident_history,
        average_speed=cq_input.traffic_flow.average_speed,
        traffic_density=cq_input.traffic_flow.traffic_density,
        incident_reports=cq_input.traffic_flow.incident_reports,
        wind_speed=cq_input.weather.wind_speed,
    )

    # validate score calculation outputs for commute quality calculation
    commute_quality_params = CommuteQualityParams(
        comfort_index=comfort_index,
        traffic_flow_efficiency=traffic_flow_efficiency,
        safety_score=safety_score,
    ).model_dump()
    commute_quality_score = calculators.calculate_overall_commute_quality_score(
        **commute_quality_params
    )
    return OverallCommuteQualitySchema(quality_score=commute_quality_score)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate commute quality based on input parameters."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str, help="Input JSON file path")
    group.add_argument("-j", "--json", type=str, help="Input JSON object as string")
    args = parser.parse_args()

    try:
        if args.file:
            input_data = load_json_file(args.file)
        if args.json:
            import ipdb

            ipdb.set_trace()
            input_data = load_json(args.json)
        else:
            print("No argument provided, check `python src/main.py --help")
        result = get_commute_quality(input_data)
        print(result.model_dump_json(indent=4))
    except (FileNotFoundError, IsADirectoryError, ValueError, ValidationError) as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
