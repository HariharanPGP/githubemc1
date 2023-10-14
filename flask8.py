from flask import *

app = Flask(__name__)

app.secret_key = "ABC"

@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None;
    if request.method == "POST":
       if request.form["pass"]  != "AAA":
          error = "Invalid user"
       else:
          flash("Successfully logged in")
          return redirect(url_for("home"))
    return render_template("log.html", error = error)


if __name__ == "__main__":
   app.run(debug = True)