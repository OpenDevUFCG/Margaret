from flask import Blueprint, request, jsonify
from python.models.organization import Organization
from python.controllers.organization_controller import OrganizationController
from python.models.user import User
import json

org = Blueprint('org', __name__, url_prefix='/organization')
organization_controller = OrganizationController()

def init_app(app):
    app.register_blueprint(org)

@org.route('/', methods=['POST'])
def add_org():
    data = request.get_json()
    ownerData = data['owner']
    owner = User(ownerData['name'], ownerData['email'], ownerData['discord_id'])
    return str(organization_controller.add_organization(data['name'], data['desc'], owner, data['category']))

@org.route('/', methods=['GET'])
def list_orgs():
    response = {}
    orgs = organization_controller.list_organizations()
    
    for i in range(len(orgs)):
        response[i + 1] = json.loads(orgs[i].to_json())

    return response

@org.route('/', methods=['DELETE'])
def remove_org():
    data = request.get_json()
    return organization_controller.remove_organization(data['org_Id']).to_json()
    
@org.route('/<int:org_id>', methods=['GET'])
def get_org(org_id):
    return organization_controller.get_organization(int(org_id)).to_json()

@org.route('/<int:org_id>', methods=['PATCH'])
def update_org(org_id):
    args = list(request.get_json().items())
    return organization_controller.modify_organization_by_atribute(org_id, args[0][0], args[0][1]).to_json()

@org.route('/search', methods=['GET'])
def search_org():
    args = list(request.args.to_dict().items())
    search_result = organization_controller.find_organization_by_atribute(args[0][0], args[0][1])

    response = {}
    for i in range(len(search_result)):
        response[i + 1] = json.loads(search_result[i].to_json())

    return response
    