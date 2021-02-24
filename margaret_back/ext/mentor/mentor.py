from flask_restx import Namespace, Resource, abort, reqparse
from flask import request
from margaret_back.controllers.mentor_controller import MentorController
from margaret_back.models.mentor import mentor_schema
import json

mentor = Namespace('Mentor', description='')

mentor_controller = MentorController()

@mentor.route('/search/')
class Mentor(Resource):

    @mentor.marshal_list_with(mentor_schema)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('attribute', type=str, help='Atribute cannot be converted')
        parser.add_argument('value', type=str help='Value cannot be converted')

        args = parser.parse_args()
        try:
            return mentor_controller.find_mentors_by_attribute(args)
        except AttributeError as attrError:
            abort(409, message=attrError)

        except ValueError as valError:
            abort(409, message=valError)

@mentor.route('/')
class Mentor(Resource):

    @mentor.marshal_list_with(mentor_schema)
    def get(self):
        return list(mentor_controller.list_mentor())

    @mentor.marshal_list_with(mentor_schema)
    def post(self):
        data = request.get_json()
        try:
            return mentor_controller.add_mentor(
                data['name'], data['email'], data['discord'], data['state'])
        except ValueError as valError:
            abort(409, message=valError)

        except AttributeError as attrError:
            abort(409, message=attrError)

    @mentor.marshal_list_with(mentor_schema)
    def delete(self):
        data = request.get_json()
        try:
            return mentor_controller.remove_mentor(data['email'])
        except ValueError as valError:
            abort(404, message=valError)

    @mentor.marshal_list_with(mentor_schema)
    def patch(self):
        data = request.get_json()
        try:
            return mentor_controller.modify_mentor_by_attribute(
                data["email"], data["atribute"], data["value"])
        except AttributeError as attrError:
            abort(409, message=attrError)
        except ValueError as valError:
            abort(404, message=valError)
