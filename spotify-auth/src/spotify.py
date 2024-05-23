from flask import session
import requests
from typing import Dict

from src.auth_token import auth_header


def get_track_data(uri: str) -> Dict | None:
    token = session.get("access_token")
    url = f"https://api.spotify.com/v1/tracks/{uri}"
    headers = auth_header(token)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    return None


def get_recently_played():
    token = session.get("access_token")
    url = "https://api.spotify.com/v1/me/player/recently-played"
    headers = auth_header(token)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    return None
