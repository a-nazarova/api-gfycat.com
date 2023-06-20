import pytest
import requests
import constant


@pytest.fixture
def response():
    print("\nexecute query for tests..")
    response = requests.get(constant.BASE_URL, headers=constant.HEADERS)
    yield response
    # этот код выполнится после завершения теста
    print("\nend of test..")
    pass

