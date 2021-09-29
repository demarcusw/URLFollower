from flask import Flask, json, request, jsonify, make_response
from constants import *
from api.linkfollower import go_follow

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == GET:
        resp = None
        return make_response(jsonify(resp), 200)

    elif request.method == POST:
        if request.is_json:
            try:
                req = request.get_json()
                url = req.get('url')
                resp = go_follow(url)

                return make_response(jsonify(resp), 200)
            except Exception as e:
                return make_response(jsonify(e), 400)

        else:
            msg = {"message": "Request body must be JSON!"}
            return make_response(jsonify(msg), 400)
    else:
        pass


if __name__ == "__main__":
    app.run()
