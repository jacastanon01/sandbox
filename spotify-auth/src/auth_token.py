from base64 import b64encode
import time
from urllib.parse import urlencode
from flask import redirect, session
import requests
from typing import TypedDict, Optional
from functools import wraps


from src.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

REDIRECT = "http://127.0.0.1:8000/callback"


class ResponseToken(TypedDict):
    access_token: str
    expires_in: int


def request_access_token():
    try:
        url = "https://accounts.spotify.com/authorize"
        scope = (
            "user-read-recently-played playlist-modify-public playlist-modify-private"
        )
        params = {
            "client_id": SPOTIFY_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": REDIRECT,
            "scope": scope,
        }

        auth_url = f"{url}?{urlencode(params)}"
        return redirect(auth_url)

    except Exception as e:
        print(f"Unable to generate new token\n{e}")


def generate_token(code: Optional[str] = None) -> ResponseToken:
    """Gets a token from the Spotify API"""
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
        if code:
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT,
            }
        else:
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


def auth_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_token_expired():
            print("Current token is still valid")
        else:
            token = generate_token()
            save_token_to_session(token)
        return func(*args, **kwargs)

    return wrapper
