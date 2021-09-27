from flask import Flask, json, request, jsonify, make_response
from constants import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == GET:
        resp = {"message": "Hello, World!"}
        res = make_response(jsonify(resp), 200)
        return res

    elif request.method == POST:
        if request.is_json:
            req = request.get_json()

            resp_body = {
                "message": "JSON Received!",
                "sender": req.get('name')
            }
            res = make_response(jsonify(resp_body), 200)
            return res

        else:
            msg = {"message": "Request body must be JSON!"}
            return make_response(jsonify(msg), 400)
    else:
        pass

if __name__ == "__main__":
    app.run()