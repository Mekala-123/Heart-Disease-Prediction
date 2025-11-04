# LHI FastAPI Project - Week 1 (Local setup)

## Run locally

1. Create virtualenv and install:
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run server:
   ```
   uvicorn src.core.app:app --reload
   ```

3. Open:
   - http://127.0.0.1:8000/health
   - http://127.0.0.1:8000/version
   - Swagger UI: http://127.0.0.1:8000/docs

4. Run tests:
   ```
   pytest -q
   ```
