from flask_restx import Api
from .organization.organization import organization

api = Api(
    title='Margaret',
    version='0.1.0',
    description='A description',
)

api.add_namespace(organization, path='/organization')

def init_app(app):
    api.init_app(app)