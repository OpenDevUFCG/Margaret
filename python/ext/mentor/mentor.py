from flask import Blueprint, request
from python.models.mentor import Mentor
from python.controllers.mentor_controller import MentorController
from python.models.user import User

mentor = Blueprint('mentor', __name__, url_prefix='/mentor')
mentor_controller = MentorController()

def init_app(app):
    app.register_blueprint(mentor)

@mentor.route('/', methods=['POST'])
def add_mentor():
    data = request.get_json()
    response = str(mentor_controller.add_mentor(data['name'], data['email'], data['discord'], data['state']))
    return response, 201

@mentor.route('/', methods=['DELETE'])
def remove_mentor():
    data = request.get_json()
    response = mentor_controller.remove_mentor(data['email'])
    return response, 200

@mentor.route('/', methods=['GET'])
def find_mentor_by_attribute():
    data = request.get_json()
    attribute = data['attribute']
    value_attribute = data['value_attribute']



