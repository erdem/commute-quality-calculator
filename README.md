# Commute Quality Calculator

## Overview
The Commute Quality Calculator is a CLI tool that uses Pydantic for data validation in a statistical model. It calculates a commute quality score based on traffic, weather, and road condition data. This project showcases practical Pydantic usage in data processing and analysis.


## Setup
 
1. Clone the repository and navigate to the root folder in your terminal.
```bash
git clone git@github.com:erdem/commute_quality_calculator.git
```

2. Install the project dependencies with poetry via call `make install` command.

```shell
make install
```

3. The project uses pre-commit to enforce code formatting and run linters before every commit. The pre-commit hooks configuration is stored in the .pre-commit-config.yaml file. Install the hooks before making any commit.

```bash
pre-commit install
```


# Usage

You can pass JSON input file path or a JSON object directly to get overall commute quality score.  

**File Path Usage:**
```shell
python src/main.py --file=samples/input3.json
```

**JSON Object Usage**
```shell
python src/main.py --json='{"weather":{"temperature":-5,"humidity":90.5,"wind_speed":25},"traffic_flow":{"average_speed":10.5,"traffic_density":[0.95,0.98,0.99],"incident_reports":10},"road_condition":{"road_quality":2,"lighting_conditions":3,"accident_history":7}}'
```

**Output:**
```shell
{
    "quality_score": -2.076320939334637,
    "commute_quality": "Poor"
}
```
