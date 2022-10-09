
def test_read_listing_success(client):
    response = client.get("/listing/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['address'] == "245 Prospect Ave. New Lenox, IL 60451"
    assert response.json()['price'] == 250000


def test_read_listing_fail(client):
    response = client.get("/listing/1000")
    assert response.status_code == 404
    response = client.get("/listing/aa")
    assert response.status_code == 422


def test_read_listings_success(client):
    response = client.get("/listing/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_listings_w_params_success(client):
    response = client.get("/listing/?skip=3&limit=5")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_read_listing_w_params_fail(client):
    response = client.get("/listing/?skip=a&limit=b")
    assert response.status_code == 422


def test_search_listing_success(client):
    response = client.get("/listing/search/north?limit=100")
    assert response.status_code == 200
    assert response.json()[0]['id'] == 5


def test_search_listing_not_found(client):
    response = client.get("/listing/search/hede?limit=100")
    assert response.status_code == 404


def test_create_listing_success(client):
    data = """
    {
        "address": "9 Harvard Drive Passaic, NJ 07055",
        "price": 900000
    }
    """
    response = client.post("/listing/", data)
    assert response.status_code == 201
    assert response.json()["address"] == "9 Harvard Drive Passaic, NJ 07055"


def test_create_listing_validation_fail(client):
    data = """
    {
        "address": "9 Harvard Drive Passaic, NJ 07055",
        "price": adad
    }
    """
    response = client.post("/listing/", data)
    assert response.status_code == 422


def test_update_listing_success(client):
    data = """
    {
        "id": 3,
        "address": "94 Peachtree Ave.Ravenna, OH 44266",
        "price": 850000
    }
    """
    response = client.put("/listing/", data)
    response.status_code == 201
    response.json()["address"] == "94 Peachtree Ave.Ravenna, OH 44266"


def test_update_listing_validation(client):
    data = """
        {
            "id": 3,
            "address": "94 Peachtree Ave.Ravenna, OH 44266",
            "price": adada
        }
        """
    response = client.put("/listing/", data)
    response.status_code == 422


def test_update_listing_not_found(client):
    data = """
        {
            "id": 300,
            "address": "94 Peachtree Ave.Ravenna, OH 44266",
            "price": 500000
        }
        """
    response = client.put("/listing/", data)
    response.status_code == 404


def test_delete_listing_success(client):
    response = client.delete("/listing/7")
    response.status_code == 200
    response.json()["id"] == 7


def test_delete_listing_not_found(client):
    response = client.delete("/listing/700")
    response.status_code == 404




