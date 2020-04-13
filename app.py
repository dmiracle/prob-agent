from pagent.agent import Agent
from pagent.population import Population
from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
import jsonpickle

app = Flask(__name__)
api = Api(app)

app_population = Population()
app_population.init_population(25)
app_agent = Agent()
app_agent.init_props()

@app.route("/<int:bars_count>/")
def chart(bars_count):
    if bars_count <= 0:
        bars_count = 1
    return render_template("chart.html", bars_count=bars_count)

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
        app_population = Population()
        app_population.init_population(25)
        app_agent = Agent()
        app_agent.init_props() 
        return jsonify(app_population.as_dict())

api.add_resource(RestEndpoint, '/pop')