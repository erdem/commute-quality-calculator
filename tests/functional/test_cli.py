import json


def test_valid_input_path(run_cli_command, valid_input_path):
    output, error, exit_code = run_cli_command(json_path=str(valid_input_path))

    assert exit_code == 0
    assert error == ""

    result = json.loads(output)
    assert result["quality_score"] == 88.35474254742546
    assert result["commute_quality"] == "Good"


def test_valid_input_json(run_cli_command, valid_input_json):
    output, error, exit_code = run_cli_command(json_obj=str(valid_input_json))

    assert exit_code == 0
    assert error == ""

    result = json.loads(output)
    assert result["quality_score"] == 88.35474254742546
    assert result["commute_quality"] == "Good"


def test_valid_input_without_optionals(run_cli_command, valid_input_without_optionals_path):
    output, error, exit_code = run_cli_command(json_path=str(valid_input_without_optionals_path))

    assert exit_code == 0
    assert error == ""

    result = json.loads(output)
    assert result["quality_score"] == 31.519445362371297
    assert result["commute_quality"] == "Average"


def test_invalid_input_path(run_cli_command, invalid_input_path):
    output, error, exit_code = run_cli_command(json_path=str(invalid_input_path))

    assert exit_code == 1
    assert "Error: Invalid input data: 3 validation errors for CommuteQualityInput" in error


def test_file_not_found(run_cli_command):
    non_existent_file = "fixtures/non_existent.json"
    output, error, exit_code = run_cli_command(json_path=non_existent_file)

    assert exit_code != 0
    assert f"Error: JSON file not found: {non_existent_file}" in error
    assert output == ""


def test_invalid_json_string(run_cli_command):
    invalid_json = "{invalid:json}"
    output, error, exit_code = run_cli_command(json_obj=invalid_json)

    assert exit_code != 0
    assert "Error: Invalid JSON Input:" in error
    assert output == ""
