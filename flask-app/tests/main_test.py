from app import app

def test_get():
    resp = app.test_client().get('/')

    assert resp.status_code == 200
    assert resp.data == b'null\n'