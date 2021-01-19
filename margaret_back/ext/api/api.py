from flask_restx import Api
from .testext import testex

api = Api(
    title='Margaret',
    version='0.1.0',
    description='A description',
)
api.add_namespace(testext, path='/testext')

def init_app(app):
    api.init_app(app)
