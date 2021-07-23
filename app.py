# source : https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
# source : https://stackoverflow.com/questions/49480243/how-to-load-a-pickle-file-containing-scikit-learn-model-in-a-flask-application
# sources : https://docs.docker.com/compose/gettingstarted/

import time

from flask import Flask, jsonify
from sklearn.externals import joblib

import pandas as pd
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)