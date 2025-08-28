Local Calorie Tracker — Django/HTMX/Tailwind/Postgres

Commands
- python3 -m venv .venv && source .venv/bin/activate
- pip install pip-tools pre-commit ruff black isort
- cd backend && pip-compile requirements.in -o requirements.txt && pip-compile requirements-dev.in -o requirements-dev.txt && pip install -r requirements.txt -r requirements-dev.txt
- pre-commit install
- make dev

Next
- A2: Postgres local setup
- A3: Django project/app scaffold
