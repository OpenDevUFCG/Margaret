from flask import Flask, jsonify
from python.project import Project

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    proj = Project("Margaret", "sistem andromedev", "projeto opensource", "back")
    return jsonify(proj.__dict__)


if __name__ == "__main__":
    app.run()