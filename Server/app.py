from flask import Flask
from flask_cors import CORS, cross_origin
from Server.src.routes import routes

app = Flask(__name__)
CORS(app)
routes.router(app)

if __name__ == '__main__':
    app.run()
