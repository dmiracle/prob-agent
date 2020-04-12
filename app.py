from pagent.agent import Agent
from pagent.population import Population
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import jsonpickle

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

class RestEndpoint(Resource):
    def get(self):
        return jsonify(app_population.as_dict())

api.add_resource(RestEndpoint, '/pop')