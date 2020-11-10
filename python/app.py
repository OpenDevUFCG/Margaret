
from flask import Flask
from python.models.subscribed import Subscribed
from python.models.user import User
from python.models.project import Project
from python.ext.mentor import mentor

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    mentor.init_app(app)
    return app


@app.route('/', methods=['GET'])
def index():
    return 'rotas:   /subscribed   -   /project   -   /subs'

@app.route('/subscribed', methods=['GET'])
def subscriber():
    subscribed = Subscribed('All Might', 'arumaito.smash@ccc.ufcg.edu.br', 'Arumaito#4586', '2002.1', '')
    return subscribed.__dict__


@app.route("/project", methods=["GET"])
def project():
    proj = Project('Margaret', 'sistem andromedev', 'projeto opensource', 'back'"aaa","aaa")
    return proj.__dict__


@app.route("/subs", methods=["GET"])
def user():
    sub = User("Caio","caio.caio@ccc.ufcg.edu.br","caio#1313")
    return sub.__dict__

if __name__ == "__main__":
    app.run()