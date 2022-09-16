from app import app
from flask import render_template, redirect, request, session, make_response, flash
from datetime import date
from repositories import user_repo, album_repo
from services import user_serv


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if user_repo.login(username, password):
      return redirect("/")
  return render_template("error.html", message="Unidentified username or incorrect password")


@app.route("/logout")
def logout():
  user_serv.logout()
  return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
  #"""
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
    
    if user_repo.register(username, password1):
      return redirect("/")
    
    return render_template("error.html", message="Account creation failed")
  

@app.route("/addalbum", methods=["GET", "POST"])
def addalbum():
  print("alussa")
  if request.method == "GET":
    return render_template("addalbum.html")

  elif request.method == "POST":
    print("vieläki alussa")
    token = request.form["csrf_token"]
    print("1")
    if user_serv.check_token(token):
      print("2")
      artist = request.form["artist"]
      print("3")
      album_name = request.form["albumname"]
      print("4")
      release_year = request.form["releaseyear"]
      if release_year == "":
        release_year = 0
      print("5")
      genre = request.form["genre"].upper()
      print("6")
      cover_image = request.files["cover_image"]
      #if not cover_image.filename.endswith(".jpg"):
      cover_image = cover_image.read()
      print("7")
      comment = request.form["comment"]
      print(request.form["comment"])
      print("8")
      grade = int(request.form["grade"])
      print("9")
      songs = []
      songs_length = {}
      song = request.form["song0"]
      if song == "":
        return render_template("addalbum.html", message_song=" An album hasto contain atleast one (1) song.")
      else:
        for i in range(11):
          song = request.form["song"+str(i)]
          if song != "":
            songs.append(song)
            minutes = request.form["min"+str(i)]
            if minutes == "":
              minutes = 0
            seconds = request.form["sec"+str(i)]
            if seconds == "":
              seconds = 0
            songs_length[minutes] = seconds
      
      print("tänne asti")

      if len(album_name) < 1 or len(album_name) > 100:
        return render_template("addalbum.html", message_album=" Album name has to be between one (1) and hundred (100) characters.")
      elif len(artist) < 1 or len(artist) > 100:
        return render_template("addalbum.html", message_artist=" Artist name has to be between one (1) and hundred (100) characters.")
      elif len(genre) > 123:
        return render_template("addalbum.html", message_genre=" Genre cannot be longer than hundred (100) characters.")
      #elif len(songs) < 1:
      #  return render_template("addalbum.html", message_song="An album hasto contain atleast one (1) song.")
      elif len(comment) > 5000:
        return render_template("addalbum.html", message_comment=" Review cannot be longer than five thousand (5000) characters.")
      elif album_repo.add_album(artist, album_name, release_year, genre, comment, cover_image, songs, songs_length, grade):
        print("täällä")
        #return redirect("/album/")
        return redirect("/")
      return render_template("addalbum.html", message_adding=" Adding the new album has failed")
    else:
      print("abortti")
      return redirect("/")


@app.route("/addreview")#, methods="POST")
def addreview():
  #comment = request.form("comment")
  #grade = request.form("grade")
  return redirect("/")


@app.route("/album/<int:id>")
def album(id:int):
  album_name = "ads"
  artist = "qwe"
  return render_template("album.html", album=album_name)


@app.route("/artist/<int:id>")
def artist(id):

  return render_template("artist.html")