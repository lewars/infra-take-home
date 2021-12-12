import os

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/reverse", methods=["POST"])
def reverse():
    a_str = ''
    rev_str_data = {}
    if request.method == "POST":
        a_str = request.data.decode()
        rev_str_data['payload'] = a_str[::-1]
    else:
        return "Bad request", 400
    return rev_str_data, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
