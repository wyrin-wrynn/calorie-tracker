PY = . .venv/bin/activate;

.PHONY: deps dev lint format test clean reset

deps:
	$(PY) cd backend && pip-compile requirements.in -o requirements.txt
	$(PY) cd backend && pip-compile requirements-dev.in -o requirements-dev.txt
	$(PY) pip install -r backend/requirements.txt -r backend/requirements-dev.txt
	pre-commit install

dev:
	@echo "Dev env ready. Django scaffold comes in A3."

lint:
	ruff check .
	isort --check-only .
	black --check .

format:
	isort .
	black .

test:
	pytest -q

clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} \; || true
	find . -name "*.pyc" -delete || true

reset:
	rm -rf .venv
