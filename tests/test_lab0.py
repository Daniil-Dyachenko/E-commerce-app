from fastapi.testclient import TestClient
from src.main import app
from src.logger import logger

client = TestClient(app)


def test_health_check_endpoint():
    logger.info("Running test: test_health_check_endpoint")
    response = client.get("/health")
    assert response.status_code in [200, 503]


def test_create_product():
    logger.info("Running test: test_create_product")
    response = client.post("/products/", json={"name": "Laptop", "price": 1500.00})
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert "id" in response.json()


def test_get_product():
    logger.info("Running test: test_get_product")
    create_response = client.post("/products/", json={"name": "Mouse", "price": 25.00})
    product_id = create_response.json()["id"]

    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Mouse"


def test_update_product():
    logger.info("Running test: test_update_product")
    create_response = client.post("/products/", json={"name": "Keyboard", "price": 50.00})
    product_id = create_response.json()["id"]

    response = client.put(f"/products/{product_id}", json={"name": "Gaming Keyboard", "price": 100.00})
    assert response.status_code == 200
    assert response.json()["name"] == "Gaming Keyboard"


def test_delete_product():
    logger.info("Running test: test_delete_product")
    create_response = client.post("/products/", json={"name": "Monitor", "price": 300.00})
    product_id = create_response.json()["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200

    response_after_delete = client.get(f"/products/{product_id}")
    assert response_after_delete.status_code == 404
    assert response_after_delete.json() == {"detail": "Product not found"}