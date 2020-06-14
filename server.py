from flask import Flask, request, jsonify
from flask_cors import CORS
from run import run_ansys


app = Flask(__name__)
CORS(app)  # local development cors


@app.route('/run_ansys', methods=["POST"])
def run_ansys():
    request_data = request.get_json()
    return jsonify(request_data)


if __name__ == "__main__":
    app.run(debug=True)
