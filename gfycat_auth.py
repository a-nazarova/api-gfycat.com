import requests


def get_token_gfycat(credentials):
    token = requests.post("https://weblogin.gfycat.com/oauth/weblogin", json=credentials)
    token_body = token.json()
    token = token_body["access_token"]
    return "Bearer " + token


credentials = {
    "grant_type": "password",
    "password": "password",
    "username": "username"
}

token_gfycat = get_token_gfycat(credentials)
