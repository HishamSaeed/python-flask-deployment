from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, world! , this is just a demo for flask . This is a demo for fenicsWeb'

@app.route('/t_start')
def getTStart():
    return jsonify({ "tStart": 32 })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')