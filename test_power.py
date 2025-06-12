from app import power_of_two

def test_power_of_two():
    test_cases = [
        (0, 1),
        (1, 2),
        (2, 4),
        (3, 8),
        (4, 16),
        (5, 32),
        (6, 64),
        (7, 128),
        (8, 256),
        (9, 512),
        (10, 1024)
    ]
    for exp, expected in test_cases:
        result = power_of_two(exp)
        assert result == expected

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"

def test_echo():
    client = app.test_client()
    payload = {"message": "hi there"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    assert response.get_json() == {"you_sent": payload}


