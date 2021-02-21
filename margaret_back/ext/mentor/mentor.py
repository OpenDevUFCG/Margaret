from flask_restx import Namespace, Resource, fields, marshal, abort
from flask import request
from margaret_back.controllers.mentor_controller import MentorController
import json

mentor = Namespace('Mentor', description='')

mentor_controller = MentorController()

mentor_model = mentor.model('ModelList', {
    "name": fields.String,
    "email": fields.String,
    "discord_id": fields.String,
    "state": fields.String,
})


@mentor.route('/search/')
class Mentor(Resource):

    @mentor.marshal_list_with(mentor_model)
    def get(self):
        data = request.get_json()
        try:
            return mentor_controller.find_mentors_by_attribute(
                data['atribute'], data['value'])
        except AttributeError as attrError:
            abort(409, message=attrError)

        except ValueError as valError:
            abort(409, message=valError)


@mentor.route('/')
class Mentor(Resource):

    @mentor.marshal_list_with(mentor_model)
    def get(self):
        return list(mentor_controller.list_mentor())

    @mentor.marshal_list_with(mentor_model)
    def post(self):
        data = request.get_json()
        try:
            return mentor_controller.add_mentor(
                data['name'], data['email'], data['discord'], data['state'])
        except ValueError as valError:
            abort(409, message=valError)

        except AttributeError as attrError:
            abort(409, message=attrError)

    @mentor.marshal_list_with(mentor_model)
    def delete(self):
        data = request.get_json()
        try:
            return mentor_controller.remove_mentor(data['email'])
        except ValueError as valError:
            abort(404, message=valError)

    @mentor.marshal_list_with(mentor_model)
    def patch(self):
        data = request.get_json()
        try:
            return mentor_controller.modify_mentor_by_attribute(
                data["email"], data["atribute"], data["value"])
        except AttributeError as attrError:
            abort(409, message=attrError)
        except ValueError as valError:
            abort(404, message=valError)
