from flask import jsonify, request
from Server.src.modules.bully_calculator_handler import calculate_bully_score
from flask_cors import cross_origin


def router(app):
    @cross_origin
    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    @cross_origin
    @app.route("/calculate", methods=["POST"])
    def calculate():
        req_json = request.get_json()
        if not req_json.get('user'):
            return app.response_class(
                response={"message": "user param is not in the json"},
                status=400,
                mimetype='application/json'
            )
        result = calculate_bully_score(req_json["user"])

        return result, 200
