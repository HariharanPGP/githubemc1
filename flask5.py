from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hi Hi Hi Hi HI"


@app.route("/call/<float:salary>")
def display(salary):
    return "my salary %f" % salary


if __name__ == "__main__":
   app.run()