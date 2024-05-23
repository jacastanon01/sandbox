from flask import Response, jsonify, session
import requests
from typing import Literal, Dict

from src.auth_token import auth_wrapper, auth_header


# @auth_wrapper
def get_track_data(uri: str) -> Dict | None:
    token = session.get("access_token")
    url = f"https://api.spotify.com/v1/tracks/{uri}"
    headers = auth_header(token)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    return None


# @auth_wrapper
def get_track(
    uri: str,
) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    token = session.get("access_token")
    data = get_track_data(token, uri)
    if data:
        return jsonify({"data": data}), 200
    else:
        return jsonify({"error": "Track not found."}), 404


def get_recently_played():
    url = "https://api.spotify.com/v1/me/player/recently-played"
