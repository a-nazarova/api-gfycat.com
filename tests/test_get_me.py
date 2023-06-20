import pytest
import requests
import constant
from datetime import datetime



@pytest.mark.smoke
def test_status_code_get_data_user_auth(response):
    """Тест проверяет статус код при запросе данных авторизованным юзером о себе"""
    assert response.status_code == 200, f"Статус код - {response.status_code}, ожидалось - 200"


@pytest.mark.smoke
def test_status_code_get_data_user_not_auth():
    """Тест проверяет статус код при запросе данных неавторизованным юзером"""
    response = requests.get(constant.BASE_URL)
    assert response.status_code == 401, f"Статус код - {response.status_code}, ожидалось - 401"


@pytest.mark.smoke
def test_verified_email_user(response):
    """Тест проверяет что email пользователя подтвержен"""
    response = response.json()
    status_email = response["emailVerified"]
    assert status_email is True, "Email пользователя не подтвержден"


@pytest.mark.smoke
def test_count_download_gif(response):
    """Тест проверяет количество gif, загруженных пользователем"""
    response = response.json()
    count_gif = response["totalGfycats"]
    assert count_gif == 14, f"Количество загруженных gif - {count_gif}, ожидалось - 14"


@pytest.mark.smoke
def test_count_views_user(response):
    """Тест проверяет, что количество просмотров пользователя больше 800"""
    response = response.json()
    count_views = response["views"]
    assert count_views > 800, f"Количество просмотров пользователя {count_views} < 800 "


@pytest.mark.smoke
def test_account_date_create(response):
    """Тест проверяет, что аккаунт создан раньше 01.02.2023"""
    response = response.json()
    date_create_acc = response["createDate"]
    date_create_acc = str(datetime.fromtimestamp(date_create_acc))
    assert date_create_acc < "2023-02-01", f"Дата создания аккаунта {date_create_acc} позже 2023-02-01 "


@pytest.mark.smoke
def test_equally_userid_and_username(response):
    """Тест проверяет, что userid равен username"""
    response = response.json()
    userid = response["userid"]
    username = response["username"]
    assert userid == username, f"Userid - {userid} неравен username - {username}"


@pytest.mark.smoke
def test_user_url(response):
    """Тест проверяет формирование персональной ссылки пользователя"""
    response = response.json()
    url_user = response["url"]
    username = response["username"]
    assert url_user == f"https://gfycat.com/@{username}", f"Ссылка пользователя {url_user} несоответсвует шаблону"


@pytest.mark.smoke
def test_absence_profile_image(response):
    """Тест проверяет отсутствие аватара пользователя"""
    response = response.json()
    status_image = response["iframeProfileImageVisible"]
    assert status_image is False, "У пользователя есть аватар"


@pytest.mark.smoke
def test_no_followers(response):
    """Тест проверяет, что у пользователя скучный контент, из-за чего нет подписчиков"""
    response = response.json()
    count_followers = response["followers"]
    assert count_followers == 0, "У пользователя есть подписчики!"
