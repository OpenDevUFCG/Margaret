from flask import Blueprint, request, abort
from margaret_back.controllers.project_controller import ProjectController
from margaret_back.models.mentor import Mentor
from margaret_back.models.user import User
import json

proj = Blueprint('proj', __name__, url_prefix='/project')
project_controller = ProjectController()

def init_app(app):
    app.register_blueprint(proj)


@proj.route('/', methods=['POST'])
def add_project():
    data = request.get_json()

    try: 
        mentor = Mentor(data['mentor_name'], data['mentor_email'], data['discord_id'], data['organization'])
        aux_mentor = Mentor(data['aux_name'], data['aux_email'], data['aux_discord_id'], data['aux_organization'])
        response = str(project_controller.add_project(data['name'], data['description'], data['base_text'], mentor, aux_mentor, data['areas']))
    except AttributeError:
        abort(400, "Attribute invalid")
    except KeyError:
        abort(400, "Attribute missing")

    return response

@proj.route('/', methods=['GET'])
def list_projs():
    response = dict()
    projs = project_controller.list_projects()

    # for i, proj in enumerate(projs):
    #     response[i + 1] = json.loads(proj.to_json())

    response = {key + 1: json.loads(value.to_json()) for (key, value) in enumerate(projs)}

    return response


@proj.route('/<int:proj_id>', methods=['DELETE'])
def remove_proj(proj_id):

    try:
        response = project_controller.remove_project(int(proj_id)).to_json()
    except IndexError:
        abort(400, "Id invalid or missing")

    return response

@proj.route('/<int:proj_id>', methods=['PUT'])
def update_proj(proj_id):
    
    # for i in len(data):
    #     project_controller.update_project_value(proj_id, data[i][0], data[i][1])
    
    try:
        data = request.get_json()
        response = project_controller.update_project_value(proj_id, data["attribute"], data["new_value"]).to_json()
    except IndexError:
        abort(400, "Id invalid or missing")
    except AttributeError:
        abort(400, "Attribute not exist")
    
    return response
