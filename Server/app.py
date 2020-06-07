from flask import Flask
from Server.controllers import routes


class App(Flask):
    def init(self):
        routes.router(self)
        return self


if __name__ == "__main__":
    app = App(__name__).init()
    app.run(host='0.0.0.0')