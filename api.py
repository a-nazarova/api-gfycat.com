import requests
import constant


def get_token_gfycat():
    """Функция возвращает авторизационный токен по логину и паролю"""
    token = requests.post("https://weblogin.gfycat.com/oauth/weblogin", json=constant.CREDENTIALS)
    token_body = token.json()
    token = token_body["access_token"]
    return "Bearer " + token




