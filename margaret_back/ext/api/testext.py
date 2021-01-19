from flask import Blueprint
from flask_restx import Namespace, Resource

testext = Namespace('Testext', description='Um namespace de zoa')

@testext.route("/")
class TestExt(Resource):
    def get(self):
        return "OK!!!!"
    def post(self):
        return "TOOOOOp"

