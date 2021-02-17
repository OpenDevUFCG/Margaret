from flask_restx import Namespace, Resource, fields
from flask import request
from margaret_back.controllers.organization_controller import \
    OrganizationController
from margaret_back.models.user import User
from margaret_back.models.organization import organization_schema


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
        ownerData = data['owner']
        owner = User(ownerData['name'], ownerData['email'],
                     ownerData['discord_id'])
        return str(organization_controller.add_organization(data['name'],
                                                            data['desc'],
                                                            owner,
                                                            data['category']))
