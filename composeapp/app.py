from flask import Flask
from redis import Redis
import os


app = Flask(__name__)
redis = Redis(host="redis",port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello Docker site visitor! U have been here {0} times'.format(redis.get('hits'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
