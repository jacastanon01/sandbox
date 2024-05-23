from flask import Response, jsonify, session
import requests
from typing import Literal, Dict

from src.auth_token import generate_token, is_token_expired, auth_header


def get_track_data(token: str, uri: str) -> Dict | None:
    url = f"https://api.spotify.com/v1/tracks/{uri}"
    headers = auth_header(token)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    return None


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
        return jsonify({"data": data}), 200
    else:
        return jsonify({"error": "Track not found."}), 404
