from fastapi.testclient import TestClient
from self_service_platform.api import app

client = TestClient(app)

def test_create_database():
    new_database = {}
    response = client.post("/api/v1/databases", json=new_database)

    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"

    # check if database was created with right attributes and id
    data = response.json()
    assert isinstance(data["id"], str)
    assert data["engine"] == "postgres"
    assert data["version"] == "16"
    assert data["environment"] == "dev"

# Test get database list response 
def test_get_database():
    response = client.get("/api/v1/databases")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    data = response.json()
    assert isinstance(data, list)

def test_get_database_from_id():
    new_database1 = {}
    response1 = client.post("/api/v1/databases", json=new_database1)

    assert response1.status_code == 201
    assert response1.headers["content-type"] == "application/json"

    # check if database was created with right attributes and id
    data1 = response1.json()
    assert isinstance(data1["id"], str)
    assert data1["engine"] == "postgres"
    assert data1["version"] == "16"
    assert data1["environment"] == "dev"

    print("\n--- DEBUG DATA1 TYPE ---", type(data1))
    print("--- DEBUG DATA1 CONTENT ---", data1)

    response2 = client.get(f"/api/v1/databases/{data1['id']}")
    
    assert response2.status_code == 200
    assert response2.headers["content-type"] == "application/json"
    data2 = response2.json()

    assert data2["id"] == data1["id"]
    assert data2["engine"] == data1["engine"]
    assert data2["version"] == data1["version"]
    assert data2["environment"] == data1["environment"]
