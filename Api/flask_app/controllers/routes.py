def router(app):
    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"
