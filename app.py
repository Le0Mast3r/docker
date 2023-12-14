from flask import Flask
from pandas import pandas
from numpy import numpy
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'hello world!'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)