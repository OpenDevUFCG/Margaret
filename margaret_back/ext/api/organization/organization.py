from flask_restx import Namespace, Resource, fields, reqparse
from flask import request
from margaret_back.controllers.organization_controller import \
    OrganizationController
from margaret_back.models.user import User
from margaret_back.models.organization import organization_schema, category_valids


organization = Namespace('Organization', description='')

organization_controller = OrganizationController()


@organization.route("/")
class Organization(Resource):

    @organization.marshal_list_with(organization_schema)
    def get(self):
        response = {}
        return organization_controller.list_organizations()

    def post(self):
        data = request.get_json()
        parser = reqparse.RequestParser()

        parser.add_argument('email_owner', type=str,
                            help='Rate cannot be converted')
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('category', type=str, choices=category_valids)
        args = parser.parse_args()
        return str(organization_controller.add_organization(args))
