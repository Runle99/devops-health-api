# DevOps Health API — CI Pipeline Demo

Small FastAPI application demonstrating automated testing and Docker image building with GitHub Actions.

## Endpoints
- `GET /` — service message
- `GET /health` — health check
- `GET /version` — API version

## Run locally
```bash
python -m pip install -r requirements-dev.txt
python -m uvicorn app:app --reload
```
Visit http://127.0.0.1:8000/docs

## Test
```bash
python -m pytest -q
```

## Docker
```bash
docker build -t devops-health-api .
docker run --rm -p 8000:8000 devops-health-api
```

## CI
On each push or pull request, GitHub Actions installs dependencies, runs pytest, and builds a Docker image. This pipeline **does not deploy to AWS or publish an image**.

## Architecture
Git push → GitHub Actions → Python tests → Docker image build
