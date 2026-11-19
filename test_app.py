from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World! We are LIVE on Render!" in response.data
