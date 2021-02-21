from flask_restx import Api
from margaret_back.ext.mentor.mentor import mentor

api = Api(
    title='Margaret',
    version='0.1.0',
    description='A description',
)

api.add_namespace(mentor, path='/mentor')


def init_app(app):
    api.init_app(app)
