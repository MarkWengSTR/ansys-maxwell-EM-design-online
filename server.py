from flask import Flask, request, jsonify
from threading import Thread
from flask_cors import CORS
from run import run_ansys
from api.validate import spec_present, data_type_validate, spec_keys_validate, ansys_overload_check
import requests
ansys_processing_count = 0

# debug
# import ipdb; ipdb.set_trace()

app = Flask(__name__)
CORS(app)  # local development cors

class BackgroundProcess(Thread):
    def __init__(self, ctx):
        Thread.__init__(self)
        self.ctx = ctx

    def run(self):
        ctx = run_ansys(self.ctx)

        response = requests.post(ctx["request"]["res_url"], json=ctx["response"], headers={'Content-type': 'application/json', 'Accept': 'text/plain'})

        print(response.status_code, response.json())

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
        "start_run_response": {"msg": "start run at background"},
        "error": {
            "validate": {"msg": ""}
            }
    }

    if spec_present(ctx) and \
            data_type_validate(ctx) and \
            spec_keys_validate(ctx) and \
            ansys_overload_check(ctx):
        thread_a = BackgroundProcess(ctx)
        thread_a.start()
    else:
        return jsonify(ctx["error"]["validate"])

    ansys_processing_count -= 1

    return jsonify(ctx["start_run_response"])


if __name__ == "__main__":
    app.run(debug=True)
