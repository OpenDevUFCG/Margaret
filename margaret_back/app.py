from flask import Flask
from margaret_back.ext.api import api


def create_app():
    app = Flask(__name__)
    organization.init_app(app)
    subscribed.init_app(app)
    api.init_app(app)
    app.config['ERROR_404_HELP'] = False
    app.config['ERROR_409_HELP'] = False

    return app
