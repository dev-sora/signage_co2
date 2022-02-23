from read_co2 import read
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return "This is CO2 WebAPI, Watalab.  Maintained by Sora."

@app.route('/getco2', methods=['GET'])
def get_co2():
    t, co2 = read()
    return jsonify({"timestamp": t, "co2": co2})