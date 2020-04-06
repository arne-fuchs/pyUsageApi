import flask
from flask import request, jsonify
import psutil
import json
from uptime import uptime

app = flask.Flask(__name__)

@app.route('/cpuinfo', methods=['GET'])
def cpuinfo():
    return jsonify({'cpu_percent': psutil.cpu_percent(interval=None,percpu=False)})

@app.route('/cpuinfopercore', methods=['GET'])
def cpuinfo():
    return jsonify({'cpu_percent': psutil.cpu_percent(interval=None,percpu=True)})

@app.route('/cpucount', methods=['GET'])
def cpucount():
    return jsonify({'cpu_count':psutil.cpu_count()})


@app.route('/temp', methods=['GET'])
def temp():
    return jsonify({'sensors_temperatures':psutil.sensors_temperatures(fahrenheit=False)})


@app.route('/netstat', methods=['GET'])
def netstats():
    return jsonify({'net_stat':psutil.net_io_counters()})


@app.route('/uptime', methods=['GET'])
def currentuptime():
    return jsonify({'uptime':uptime()})


@app.route('/memoryinfo', methods=['GET'])
def memoryinfo():
    return dict(psutil.virtual_memory()._asdict())


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)

