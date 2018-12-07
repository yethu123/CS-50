#from flask import Flask, redirect, render_template, request

# Configure app
#app = Flask(__name__)

'''Registrants
students = []
from flask import Flask, render_template, request,redirect

@app.route("/")
def index():
    return render_template("index.html")
#@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    return render_template("success.html")

'''
'''
@app.route("/registrants")
def registrants():
    return render_template("registrants.html", students=students)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    students.append(f"{name} from {dorm}")
    return redirect("/registrants")
    '''

''''
import os
import smtplib
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    if not name or not email or not dorm:
        return render_template("failure.html")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("jharvard@cs50.net", os.getenv("PASSWORD"))
    server.sendmail("jharvard@cs50.net", email, message)
    return render_template("success.html")
    '''
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    file = open("registrants.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("dorm")))
    file.close()
    return render_template("success.html")