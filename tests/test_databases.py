from fastapi.testclient import TestClient
from self_service_platform.api import app

client = TestClient(app)

def test_create_database():
    new_database = {"name": "Harry Potter"}
    response = client.post("/api/v1/databases", json=new_database)

    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"

    # check if database was created    
    data = response.json()
    assert data["name"] == "Harry Potter"
    assert data["engine"] == "postgres"
    assert data["version"] == "16"
    assert data["environment"] == "dev" 

def test_get_database():
    response = client.get("/api/v1/databases")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    data = response.json()
    assert isinstance(data, list)