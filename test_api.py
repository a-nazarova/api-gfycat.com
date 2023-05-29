import requests
import pytest
from datetime import datetime
from gfycat_auth import token_gfycat

url = f"https://api.gfycat.com/v1"
headers = {"Authorization": token_gfycat}
invalid_headers = {"Authorization": "1234567890"}


class TestGetMe:
    def test_status_code_get_data_user_auth(self):
        # Тест проверяет статус код при запросе данных авторизованным юзером о себе
        response = requests.get(f"{url}/me", headers=headers)
        assert response.status_code == 200, f"Статус код - {response.status_code}, ожидалось - 200"

    def test_status_code_get_data_user_not_auth(self):
        # Тест проверяет статус код при запросе данных неавторизованным юзером
        response = requests.get(f"{url}/me")
        assert response.status_code == 401, f"Статус код - {response.status_code}, ожидалось - 200"

    def test_verified_email_user(self):
        # Тест проверяет что email пользователя подтвержен
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        status_email = response["emailVerified"]
        assert status_email is True, "Email пользователя не подтвержден"

    def test_count_download_gif(self):
        # Тест проверяет количество gif, загруженных пользователем
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        count_gif = response["totalGfycats"]
        assert count_gif == 14, f"Количество загруженных gif - {count_gif}, ожидалось - 14"

    def test_count_views_user(self):
        # Тест проверяет, что количество просмотров пользователя больше 800
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        count_views = response["views"]
        assert count_views > 800, f"Количество просмотров пользователя {count_views} < 800 "

    def test_account_date_create(self):
        # Тест проверяет, что аккаунт создан раньше 01.02.2023
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        date_create_acc = response["createDate"]
        date_create_acc = str(datetime.fromtimestamp(date_create_acc))
        assert date_create_acc < "2023-02-01", f"Дата создания аккаунта {date_create_acc} позже 2023-02-01 "

    def test_equally_userid_and_username(self):
        # Тест проверяет, что userid равен username
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        userid = response["userid"]
        username = response["username"]
        assert userid == username, f"Userid - {userid} неравен username - {username}"

    def test_user_url(self):
        # Тест проверяет формирование персональной ссылки пользователя
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        url_user = response["url"]
        username = response["username"]
        assert url_user == f"https://gfycat.com/@{username}", f"Ссылка пользователя {url_user} несоответсвует шаблону"

    def test_absence_profile_image(self):
        # Тест проверяет отсутствие аватара пользователя
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        status_image = response["iframeProfileImageVisible"]
        assert status_image is False, "У пользователя есть аватар"

    def test_no_followers(self):
        # Тест проверяет, что у пользователя скучный контент, из-за чего нет подписчиков
        response = requests.get(f"{url}/me", headers=headers)
        response = response.json()
        count_followers = response["followers"]
        assert count_followers == 0, "У пользователя есть подписчики!"
