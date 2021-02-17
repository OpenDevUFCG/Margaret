from flask import Flask
from margaret_back.models.subscribed import Subscribed
from margaret_back.models.user import User
from margaret_back.models.project import Project
from margaret_back.controllers.project_controller import ProjectController
from margaret_back.ext.organization import organization
from margaret_back.ext.subscribed import subscribed
from margaret_back.ext.project import project

def create_app():
    app = Flask(__name__)
    organization.init_app(app)
    subscribed.init_app(app)
    project.init_app(app)
    return app
