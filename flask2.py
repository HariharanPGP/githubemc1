from flask import Flask

app = Flask(__name__)

@app.route("/")


@app.route("/home")
def home():
    return "HOME"


@app.route("/user/<username>")
def display(username):
    return f'Hellllooo {username}'




if __name__ == "__main__":
   app.run()