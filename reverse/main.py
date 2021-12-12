import os
import json
import requests

from flask import Flask
from flask import request

app = Flask(__name__)

URL = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT"

@app.route("/reverse", methods=["POST"])
def reverse():
    rev_str_data = {}
    if request.method == "POST":
        rev_str = request.data.decode()[::-1]
        input_str = {'INPUT': rev_str}
        rv = requests.post(URL, json = input_str,
                             headers = {'Content-Type': 'application/json'})
        data = rv.json()
        rev_str_data['payload'] = data['OUTPUT']
    else:
        return "Bad request", 400
    return rev_str_data, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
