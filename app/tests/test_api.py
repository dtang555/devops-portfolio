def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_ready(client):
    assert client.get("/ready").json() == {"status": "ready"}


def test_metrics_exposed(client):
    client.get("/health")
    body = client.get("/metrics").text
    assert "http_requests_total" in body


def test_task_crud_flow(client):
    created = client.post("/tasks", json={"title": "write runbook"})
    assert created.status_code == 201
    task_id = created.json()["id"]

    assert client.get(f"/tasks/{task_id}").json()["title"] == "write runbook"
    assert len(client.get("/tasks").json()) == 1

    patched = client.patch(f"/tasks/{task_id}", json={"done": True})
    assert patched.json()["done"] is True

    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404


def test_validation_rejects_empty_title(client):
    assert client.post("/tasks", json={"title": ""}).status_code == 422


def test_missing_task_returns_404(client):
    assert client.patch("/tasks/999", json={"done": True}).status_code == 404
    assert client.delete("/tasks/999").status_code == 404
