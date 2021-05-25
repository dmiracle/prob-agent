from pagent.agent import Agent
from pagent.population import Population

from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
import jsonpickle

import random

app = Flask(__name__)
api = Api(app)

app_population = Population()
app_population.init_population(25)
app_agent = Agent()
app_agent.init_props()

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route("/distribution")
def distro():
    return jsonify(app_agent.dist.distributions)

@app.route("/props")
def props():
    app_agent = Agent()
    app_agent.init_props()
    return jsonify(app_agent.as_dict())

@app.route("/drops")
def dropdown():
    names = ['Wi', 'Drew', 'Kevin', 'Bob']
    return render_template('test.html', names=names)

class RestEndpoint(Resource):
    def get(self):
        app_population = Population()
        app_population.init_population(25)
        app_agent = Agent()
        app_agent.init_props() 
        return jsonify(app_population.as_dict())

api.add_resource(RestEndpoint, '/pop')