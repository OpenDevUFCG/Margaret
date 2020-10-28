from flask import Flask, jsonify
from python.models.subscribed import Subscribed
from python.models.project import Project

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'rotas:   /subscribed   -   /project'

@app.route('/subscribed', methods=['GET'])
def subscriber():
    subscribed = Subscribed('All Might', 'arumaito.smash@ccc.ufcg.edu.br', 'Arumaito#4586', '2002.1', '')
    return subscribed.__dict__

@app.route('/project', methods=['GET'])
def project():
    proj = Project('Margaret', 'sistem andromedev', 'projeto opensource', 'back')
    return jsonify(proj.__dict__)


if __name__ == '__main__':
    app.run()