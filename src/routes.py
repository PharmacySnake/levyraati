from app import app
from flask import render_template, redirect, request, session, make_response
from db import db
import users

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  """
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
      return redirect("/")
  return render_template("error.html", message="Unidentified username or incorrect password")
  """
  if request.method == "GET":
    return render_template("login.html")
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
      return redirect("/")
    else:
      return render_template("error.html", message="Väärä tunnus tai salasana")


@app.route("/logout")
def logout():
  users.logout()
  return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
  """
  if request.method == "GET":
    return render_template("register.html")
  elif request.method == "POST":
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    
    if len(username) < 1:
      return render_template("error.html", message="Username is too short.\nUsername has to be between one (1) and twentytwo (22) characters.\n")
    elif len(username) > 23:
      return render_template("error.html", message="Username is too short.\nUsername has to be between one (1) and twentytwo (22) characters.\n")
    
    if len(password1) < 8:
      return render_template("error.html", message="Password should be between eight (8) and thirtytwo (32) characters")
    elif len(password1) > 32:
      return render_template("error.html", message="Password should be between eight (8) and thirtytwo (32) characters")
    elif password1 != password2:
      return render_template("error.html", message="Passwords do not match")
    
    if users.register(username, password1):
      return redirect("/")
    
    return render_template("error.html", message="Account creation failed")
  """
  if request.method == "GET":
    return render_template("register.html")
  if request.method == "POST":
    username = request.form["username"]

    if len(username) < 1:
      return render_template("error.html", message="Käyttäjänimi on liian lyhyt")
    elif len(username) > 23:
      return render_template("error.html", message="Käyttäjätunnus on liian pitkä")

    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if len(password1) < 3:
      return render_template("error.html", message="Salasana on liian lyhyt")
    elif len(password1) > 32:
      return render_template("error.html", message="Salasana on liian pitkä")
    elif password1 != password2:
      return render_template("error.html", message="Salasanat eroavat")
    if users.register(username, password1):
      return redirect("/")
    else:
      return render_template("error.html", message="Rekisteröinti ei onnistunut")