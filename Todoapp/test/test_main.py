from fastapi.testclient import TestClient

import main
from fastapi import status
Client = TestClient(main.app)
def Test_return_healthcheck():
    response = Client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'ok'}
