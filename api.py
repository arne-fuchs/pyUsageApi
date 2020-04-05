import flask
from flask import request, jsonify
import psutil
from uptime import uptime

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/cpuinfo', methods=['GET'])
def cpuinfo():
    return str(psutil.cpu_percent())


@app.route('/cpucount', methods=['GET'])
def cpucount():
    return str(psutil.cpu_count())


@app.route('/temp', methods=['GET'])
def temp():
    return str(psutil.sensors_temperatures(fahrenheit=False))


@app.route('/netstat', methods=['GET'])
def netstats():
    return str(psutil.net_io_counters())


@app.route('/uptime', methods=['GET'])
def currentuptime():
    return str(uptime())


@app.route('/memoryinfo', methods=['GET'])
def memoryinfo():
    return dict(psutil.virtual_memory()._asdict())

app.run()
