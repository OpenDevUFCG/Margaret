from flask import Blueprint, request,jsonify, abort
from python.models.subscribed import Subscribed
from python.controllers.subscribeds_controller import SubscribedsController
from python.models.user import User
import json

sub = Blueprint('sub',__name__, url_prefix='/subscribed')
subsController = SubscribedsController()

def init_app(app):
    app.register_blueprint(sub)

@sub.route('/', methods = ['POST'])
def add_sub():
    data = request.get_json()
    try:
        subs = subsController.add_subscriber(data['name'],data['email'],data['discord_id'],data['period'],data['minority_group'])
    except AttributeError:
        abort(400,"Atributos inválidos")
    except ValueError:
        abort(400,"Email já em uso")
    return subs.__dict__

@sub.route('/', methods = ['GET'])
def list_sub():
    result = {}
    subs = subsController.list_subscribeds()

    for i in range (len(subs)):
        result[i + 1] = json.loads(subs[i].to_json())
    
    return result

@sub.route('/', methods = ['DELETE'])
def remove_sub():
    data = request.get_json()
    try:
        result = subsController.remove_subscribed(data['email_user']).to_json()       
    except ValueError:
        abort(404,"Usuário não inscrito")
    
    return result

@sub.route('/<string:email_sub>', methods = ['GET'])
def get_sub(email_sub):
    data = email_sub + "@ccc.ufcg.edu.br"
    try: 
        result = subsController.get_subscribed(data).to_json()
    except ValueError:
        abort(404, "Usuário não inscrito")
    return result

@sub.route('/<string:email_sub>', methods = ['POST'])
def modify_sub(email_sub):
    email_sub = email_sub + "@ccc.ufcg.edu.br"
    data = request.get_json()
    try:
        subsController.modify_subscribed_by_attribute(email_sub, data['attribute'],data['new_attribute'])    
    except AttributeError:
        abort(400,"Atributos inválidos")
    except ValueError:
        abort(404,"Usuário não inscrito")    

    return subsController.get_subscribed(email_sub).to_json()
    

@sub.route('/search', methods = ['GET'])
def search_sub():
    data = request.get_json()
    try:
        founds = subsController.find_subscribed_by_attribute(data['attribute'],data['value_attribute'])
    except AttributeError:
        abort(400,"Atributos inválidos")
    
    result = {}

    for i in range (len(founds)):
        result[i + 1] = json.loads(founds[i].to_json())

    return result