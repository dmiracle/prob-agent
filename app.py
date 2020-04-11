from pagent.agent import Agent
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

app_agent = Agent()
app_agent.init_props()
dist_json = json.dumps(app_agent.dist.distributions)

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
    app_agent.props['Name'] = app_agent.name
    app_agent.props['UUID'] = app_agent.uid
    return jsonify(app_agent.props)