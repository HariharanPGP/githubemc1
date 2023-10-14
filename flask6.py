from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/nextpage")


@app.route("/nextpage")
def nextMethod():
    return "Hi i am in next page"




if __name__ == "__main__":
   app.run()