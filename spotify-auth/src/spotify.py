from base64 import b64encode
import time
from flask import Response, jsonify, session
import requests
from typing import Literal, TypedDict, Dict

from src.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


class ResponseToken(TypedDict):
    access_token: str
    expires_in: int


def generate_token() -> ResponseToken:
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
        data = {"grant_type": "client_credentials"}

        response = requests.post(url, headers=headers, data=data)
        token = response.json()

        save_token_to_session(token)
        return token

    except Exception as e:
        raise Exception("Unable to generate new token", str(e))


def auth_header(token: str) -> dict[str, str]:
    return {"Authorization": "Bearer " + token}


def get_track_data(token: str, uri: str) -> Dict | None:
    url = f"https://api.spotify.com/v1/tracks/{uri}"
    headers = auth_header(token)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    return None


def save_token_to_session(token) -> None:
    session["access_token"] = token.get("access_token")
    session["expires_in"] = int(time.time()) + token.get("expires_in")


def is_token_expired() -> bool:
    print(f"From is_token_expired {session.get('access_token')}")
    if session.get("access_token") is None:
        return True
    expires_at = session["expires_in"]
    return time.time() > expires_at


def get_track(
    uri: str,
) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    if session.get("access_token") is None or is_token_expired():
        gen_token = generate_token()
        token = gen_token.get("access_token")
    else:
        token = session.get("access_token")
    data = get_track_data(token, uri)
    if data:
        return requests.jsonify({"data": data}), 200
    else:
        return jsonify({"error": "Track not found."}), 404
