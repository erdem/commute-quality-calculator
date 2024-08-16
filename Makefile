install:
	poetry install --no-root

dev:
	poetry run fastapi dev src/main.py

test:
	poetry run python src/tests.py

black:
	poetry run black .

isort:
	poetry run isort .

run_tests:
	poetry run pytest .

.PHONY: install dev
