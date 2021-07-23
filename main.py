#source : https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
#source : https://stackoverflow.com/questions/49480243/how-to-load-a-pickle-file-containing-scikit-learn-model-in-a-flask-application

from flask import Flask, jsonify
from sklearn.externals import joblib

import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     return 'hello world'

if __name__ == '__main__':
     clf = joblib.load('model.pkl')
     model_columns = joblib.load('model_columns.pkl')
     app.run(port=8080)