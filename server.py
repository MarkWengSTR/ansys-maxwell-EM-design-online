from flask import Flask, request, jsonify
from flask_cors import CORS
from run import run_ansys
from api.validate import spec_present, data_type_validate, spec_keys_validate, ansys_overload_check
ansys_processing_count = 0


app = Flask(__name__)
CORS(app)  # local development cors


@app.route('/run_simu', methods=["POST"])
def run_simulation():
    global ansys_processing_count
    ansys_processing_count += 1

    ctx = {
        "request": request.get_json(),
        "allow_run": True,
        "process": {
            "limit": 4,
            "count": ansys_processing_count,
        },
        "error": {
            "validate": {"msg": ""}
            }
    }

    if spec_present(ctx) and \
            data_type_validate(ctx) and \
            spec_keys_validate(ctx) and \
            ansys_overload_check(ctx):
        ctx = run_ansys(ctx)
    else:
        return jsonify(ctx["error"]["validate"])

    ansys_processing_count -= 1

    return jsonify(ctx["response"])


if __name__ == "__main__":
    app.run(debug=True)
