'''from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    for item in request.form:
        session[item] = int(request.form.get(item))
    return redirect("/cart")


@app.route("/cart")
def cart():
    return render_template("cart.html", cart=session)'''

from flask import Flask, render_template, request

from cs50 import eprint, SQL

app = Flask(__name__)

db = SQL("sqlite:///lecture.db")

'''@app.route("/")
def index():
    rows = db.execute("SELECT * FROM Album")
    return render_template("index.html", albums=rows)
    '''
@app.route("/")
def index():
    query = request.args.get("q")
    eprint(query)
    rows = db.execute("SELECT * FROM Album WHERE Title = :q", q=query)
    return render_template("index.html", albums=rows)