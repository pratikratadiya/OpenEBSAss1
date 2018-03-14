from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0)

app = Flask(__name__)


@app.route("/")
def hello():
  
    html = "<h3>Hello {name}</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv('username'), hostname=socket.gethostname())


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
