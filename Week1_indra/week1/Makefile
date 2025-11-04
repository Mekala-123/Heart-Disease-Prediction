run:
	uvicorn src.core.app:app --reload

lint:
	pylint src || true

test:
	pytest -q

format:
	black src tests
