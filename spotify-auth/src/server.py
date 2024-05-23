from typing import Literal
from flask import jsonify, request, session, Flask, Response
import os

from src.auth_token import (
    auth_wrapper,
    request_access_token,
    save_token_to_session,
    generate_token,
    is_token_expired,
)
from src.spotify import (
    get_track_data,
)

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index() -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
    if session.get("access_token") is None or is_token_expired():
        return request_access_token()
    return jsonify({"error": "Token exists and is valid"}), 200


@app.route("/callback")  # ?code=<string:code>&state=<string:state>
@auth_wrapper
def callback() -> Response:
    print("Redirected to callback")
    code = request.args.get("code")
    if code:
        gen_token = generate_token(code)
        token = gen_token.get("access_token")
    else:
        token = session.get("access_token")
    uri = "2TpxZ7JUBn3uw46aR7qd6V"
    data = get_track_data(uri)

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


@app.route("/favicon.ico")
def favicon():
    return Response(status=204)  # No Content


if __name__ == "__main__":
    app.run()
