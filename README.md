# DevOps Portfolio: Task API on Azure

A small FastAPI service used as the vehicle for a complete delivery pipeline:
Docker, GitHub Actions, Terraform, AKS, Helm, Prometheus/Grafana.

> Status: Week 1 (app, container, CI). See `docs/` for architecture, runbooks, postmortems as they are added.

## Run locally
```bash
docker compose up --build
curl localhost:8000/health
curl -X POST localhost:8000/tasks -H 'content-type: application/json' -d '{"title":"hello"}'
```

## Develop and test
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r app/requirements-dev.txt
pytest --cov
ruff check . && ruff format --check .
```

## Endpoints
`GET /health` (liveness) · `GET /ready` (DB check) · `GET /metrics` (Prometheus) · `/tasks` CRUD

## Roadmap
- [x] Week 1: API, Dockerfile, compose, CI (lint, audit, tests, Trivy)
- [ ] Week 2: Terraform (ACR, AKS, Key Vault, Postgres), OIDC push to ACR, Checkov
- [ ] Week 3: Helm chart, automated deploy + rollback, secrets from Key Vault
- [ ] Week 4: Prometheus/Grafana + SLO alert, failure-injection postmortems, AI log summarizer
