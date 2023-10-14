Broadcast to all
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hi i am in home"


@app.route("/index")
def indexMethod():
    return "I am in index"




if __name__ == "__main__":
   app.run()