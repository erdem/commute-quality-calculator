import json
import subprocess
from pathlib import Path
from typing import Dict, Any, Callable

import pytest


TEST_DIR = Path(__file__).parent
BASE_DIR = TEST_DIR.parent
MAIN_SCRIPT = BASE_DIR.joinpath("src/main.py")


def load_json_file(file_path: Path) -> Dict[Any, Any]:
    path = Path(file_path)
    with path.open("r") as f:
        return json.loads(f.read())


@pytest.fixture
def valid_input_path():
    return TEST_DIR.joinpath("fixtures/valid_input.json")


@pytest.fixture
def valid_input_without_optionals_path():
    return TEST_DIR.joinpath("fixtures/valid_input_without_optionals.json")


@pytest.fixture
def invalid_input_path():
    return TEST_DIR.joinpath("fixtures/invalid_input.json")


@pytest.fixture
def valid_input_json(valid_input_path):
    data = load_json_file(valid_input_path)
    return json.dumps(data)


@pytest.fixture
def run_cli_command() -> Callable:
    def _run_cli_command(json_obj: str = None, json_path: str = None):
        command_template = ["python", str(MAIN_SCRIPT)]
        if json_obj is not None:
            command_template.extend(("--json", json_obj))
        if json_path is not None:
            command_template.extend(("--file", str(json_path)))

        result = subprocess.run(command_template, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode

    return _run_cli_command
