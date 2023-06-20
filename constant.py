from api import get_token_gfycat

CREDENTIALS: dict = {
    "grant_type": "password",
    "password": "Mus64103",
    "username": "a_nazarova"
}
BASE_URL: str = f"https://api.gfycat.com/v1/me"
HEADERS: dict = {"Authorization": get_token_gfycat()}
INVALID_HEADERS: dict = {"Authorization": "1234567890"}

