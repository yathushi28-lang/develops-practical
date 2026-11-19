from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"CI/CD and Docker Pipeline is a massive success! V2" in response.data
