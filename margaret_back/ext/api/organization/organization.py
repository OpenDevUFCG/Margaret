from flask_restx import Namespace, Resource, fields
from flask import request
from margaret_back.controllers.organization_controller import \
    OrganizationController
from margaret_back.models.user import User


organization = Namespace('Organization', description='')

organization_controller = OrganizationController()

user_model = organization.model('User', {
    'owner': fields.String,
    'email': fields.String,
    'discord_id': fields.String,
})

organization_model = organization.model('OrganizationList', {
    "owner": fields.Nested(user_model),
    "name":  fields.String,
    "desc":  fields.String,
    "category":  fields.String,
})


@organization.route("/")
class Organization(Resource):

    @organization.marshal_list_with(organization_model)
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
