from base64 import b64encode
import time
from flask import session
import requests
from typing import TypedDict

from src.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


class ResponseToken(TypedDict):
    access_token: str
    expires_in: int


def generate_token_from_auth_code() -> ResponseToken:
    try:
        url = "https://accounts.spotify.com/authorize"
        scope = (
            "user-read-recently-played playlist-modify-public playlist-modify-private"
        )
        params = {
            "client_id": SPOTIFY_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": "http://localhost/callback",
            "scope": scope,
        }

        response = requests.get(url, params=params)
        print(response.json())
    except Exception as e:
        print(f"Unable to generate new token/n{e}")


def generate_token_from_credentials() -> ResponseToken:
    """uses the client id and secret to get a token from the Spotify API

    Raises:
        Exception: unable to get token

    Returns:
        ResponseToken
    """
    try:
        url = "https://accounts.spotify.com/api/token"
        client_secret = SPOTIFY_CLIENT_SECRET
        client_id = SPOTIFY_CLIENT_ID

        auth_bytes = f"{client_id}:{client_secret}".encode()
        auth_header = b64encode(auth_bytes).decode()
        headers = {
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        response = requests.post(url, headers=headers, data=data)
        token = response.json()

        save_token_to_session(token)
        return token

    except Exception as e:
        raise Exception("Unable to generate new token", str(e))


def auth_header(token: str) -> dict[str, str]:
    return {"Authorization": "Bearer " + token}


def save_token_to_session(token) -> None:
    session["access_token"] = token.get("access_token")
    session["expires_in"] = int(time.time()) + token.get("expires_in")


def is_token_expired() -> bool:
    print(f"From is_token_expired {session.get('access_token')}")
    if session.get("access_token") is None:
        return True
    expires_at = session["expires_in"]
    return time.time() > expires_at


if __name__ == "__main__":
    generate_token_from_auth_code()
