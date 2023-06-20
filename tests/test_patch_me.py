import requests
import random
import pytest
import constant

@pytest.mark.regression
def test_status_code_add_description():
    """Тест проверяет успешный статус код при добавлении описания профиля"""
    request_body: dict = {
        "operations":
            [{
                "op": "add",
                "path": "/description",
                "value": "Самые смешные gif тут"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    assert response.status_code == 204, f"Статус код - {response.status_code}, ожидалось - 204"

@pytest.mark.regression
def test_status_code_remove_descritpion():
    """Тест проверяет успешный статус код при удалении описания профиля"""
    request_body: dict = {
        "operations":
            [{
                "op": "remove",
                "path": "/description"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    assert response.status_code == 204, f"Статус код - {response.status_code}, ожидалось - 204"

@pytest.mark.regression
def test_status_code_add_description_no_auth():
    """Тест проверяет успешный статус код при добавлении описания профиля без авторизации"""
    request_body: dict = {
        "operations":
            [{
                "op": "add",
                "path": "/description",
                "value": "Новое описание профиля"
            }]
    }
    response = requests.patch(constant.BASE_URL, json=request_body)
    assert response.status_code == 401, f"Статус код - {response.status_code}, ожидалось - 401"

@pytest.mark.regression
def test_status_code_add_website():
    """Тест проверяет успешный статус код при добавлении вебсайта в профиль"""
    request_body: dict = {
        "operations":
            [{
                "op": "add",
                "path": "/profile_url",
                "value": f"http://my_{random.randint(10, 99)}site.com"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    assert response.status_code == 204, f"Статус код - {response.status_code}, ожидалось - 204"

@pytest.mark.regression
def test_status_code_add_invalid_website():
    """Тест проверяет успешный статус код при добавлении описания профиля"""
    request_body: dict = {
        "operations":
            [{
                "op": "add",
                "path": "/profile_url",
                "value": "мой_сайт.ру"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    assert response.status_code == 400, f"Статус код - {response.status_code}, ожидалось - 400"

@pytest.mark.regression
def test_invalid_command():
    """Тест проверяет статус код при передаче несуществующей команды к описанию профиля"""
    request_body: dict = {
        "operations":
            [{
                "op": "delete",
                "path": "/description"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    assert response.status_code == 400, f"Статус код - {response.status_code}, ожидалось - 400"

@pytest.mark.regression
def test_invalid_path():
    """Тест проверяет статус код при передаче несущетсвующего пути"""
    request_body: dict = {
        "operations":
            [{
                "op": "remove",
                "path": "/account"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    assert response.status_code == 400, f"Статус код - {response.status_code}, ожидалось - 400"

@pytest.mark.regression
def test_status_code_empty_body():
    """Тест проверяет статус код  и мессадж запроса с пустым телом"""
    request_body = {}
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    status_code = response.status_code
    response = response.json()
    description = response["description"]
    assert status_code == 400, f"Статус код - {status_code}, ожидалось - 400"
    assert description == "Invalid JSON", f"Мессадж ошибки - {description} не соответсвует ожидаемому Invalid JSON"

@pytest.mark.regression
def test_add_empty_name():
    """Тест првоеряет статус код и мессадж при передаче пустого имени"""
    request_body: dict = {
        "operations":
            [{
                "op": "add",
                "path": "name",
                "value": ""
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    status_code = response.status_code
    response = response.json()
    description = response["description"]
    assert status_code == 400, f"Статус код - {status_code}, ожидалось - 400"
    assert description == "InvalidName", f"Мессадж ошибки - {description} не соответсвует ожидаемому InvalidName"

@pytest.mark.regression
def test_body_no_operation():
    """Тест проверяет статус код и мессадж при отсутсвии обзятельного параметра операции"""
    request_body: dict = {
        "operations":
            [{
                "path": "/profile_url",
                "value": "мой_сайт.ру"
            }]
    }
    response = requests.patch(constant.BASE_URL, headers=constant.HEADERS, json=request_body)
    status_code = response.status_code
    response = response.json()
    description = response["description"]
    assert status_code == 400, f"Статус код - {status_code}, ожидалось - 400"
    assert description == "MissingParameter", f"Мессадж ошибки - {description} не соответсвует ожидаемому MissingParameter"
