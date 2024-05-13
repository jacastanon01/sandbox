from typing import Literal
from flask import jsonify, session, Flask, Response
import os

from src.spotify import (
    generate_token,
    get_track_data,
    is_token_expired,
    save_token_to_session,
)

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index() -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    if session.get("access_token") is None or is_token_expired():
        gen_token = generate_token()
        token = gen_token.get("access_token")
    else:
        token = session.get("access_token")
    uri = "2TpxZ7JUBn3uw46aR7qd6V"
    data = get_track_data(token, uri)
    if data:
        return jsonify({"data": data}), 200
    else:
        return jsonify({"error": "Unable to retrieve data"}), 404


@app.route("/token")
def get_token() -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    try:
        access_token = generate_token()
        save_token_to_session(access_token)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify({"access_token": session.get("access_token", "")}), 200


if __name__ == "__main__":
    app.run()
