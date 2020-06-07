from flask import jsonify, request
from Server.src.modules.bully_calculator_handler import calculate_bully_score


def router(app):
    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    @app.route("/calculate", methods=["POST"])
    def calculate():
        req_json = request.get_json()
        if not req_json.get('user'):
            return app.response_class(
                response=jsonify({"message": "user param is not in the json"}),
                status=400,
                mimetype='application/json'
            )
        score, message = calculate_bully_score(req_json)

        response = app.response_class(
            response=jsonify({"message": message, "score": score}),
            status=200 if score else 400,
            mimetype='application/json'
        )
        return response
