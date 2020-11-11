from flask import Flask

from python.models.subscribed import Subscribed
from python.models.user import User
from python.models.project import Project
from python.controllers.project_controller import ProjectController
from python.ext.organization import organization
from python.ext.subscribed import subscribed

from python.util.environment import get_env

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    organization.init_app(app)
    subscribed.init_app(app)

    return app

if __name__ == "__main__":
    app.run(host=get_env("HOST"), port=get_env("PORT"))
