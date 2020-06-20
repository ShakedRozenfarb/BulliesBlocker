from flask import jsonify, request
from Server.src.modules.bully_calculator_handler import calculate_bully_score
from Server.src.modules.user_latest_tweets import search_users
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

    @cross_origin
    @app.route("/searchUsers", methods=["POST"])
    def search_users_by_text():
        req_json = request.get_json()
        if not req_json.get('search_text'):
            return app.response_class(
                response={"message": "search_text param is not in the json"},
                status=400,
                mimetype='application/json'
            )
        result = search_users(req_json["search_text"], 20)
        return jsonify(result), 200
