import requests


def get_token_gfycat(credentials):
    token = requests.post("https://weblogin.gfycat.com/oauth/weblogin", json=credentials)
    token_body = token.json()
    token = token_body["access_token"]
    return "Bearer " + token


credentials = {
    "grant_type": "password",
    "password": "Mus64103",
    "username": "a_nazarova"
}

token_gfycat = get_token_gfycat(credentials)
