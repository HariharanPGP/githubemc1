from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return "welcome %s" % name


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
       user = request.form['fname']
       return redirect(url_for('success', name = user))





if __name__ == "__main__":
   app.run()