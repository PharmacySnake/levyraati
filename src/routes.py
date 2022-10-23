from base64 import b64encode
import re
from app import app
from flask import render_template, redirect, request, session, \
                  make_response, flash
from repositories import image_repo, review_repo, song_repo, \
                         user_repo, album_repo, thumb_repo
from services import user_serv


@app.route("/")
def home():
  albums = album_repo.display_albums_home()
  images = encode_images_in_albums(albums)
  return render_template("home.html", albums=albums, images=images, len=len(albums))#, imagee=imagee)


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if user_repo.login(username, password):
      return redirect("/")
  return render_template("login.html", login_error_message ="Unidentified username or incorrect password")


@app.route("/logout")
def logout():
  user_serv.logout()
  return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  elif request.method == "POST":
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    try:
      admin = request.form["admin"]
    except:
      admin = False
    
    if len(username) < 1:
      return render_template("register.html", message_user="Username is too short.\nUsername has to be between one (1) and twentytwo (22) characters.\n")
    elif len(username) > 23:
      return render_template("register.html", message_user="Username is too short.\nUsername has to be between one (1) and twentytwo (22) characters.\n")
    elif user_repo.check_username_availability(username):
      return render_template("register.html", message_user="Username is taken.")
    if len(password1) < 8:
      return render_template("register.html", message_password="Password should be between eight (8) and thirtytwo (32) characters")
    elif len(password1) > 32:
      return render_template("register.html", message_password="Password should be between eight (8) and thirtytwo (32) characters")
    elif password1 != password2:
      return render_template("register.html", message_password="Passwords do not match")
    
    if user_repo.register(username, password1, admin):
      return redirect("/")
    
    return render_template("register.html", message="Account creation failed")
  

@app.route("/addalbum", methods=["GET", "POST"])
def addalbum():
  if request.method == "GET":
    return render_template("addalbum.html")

  elif request.method == "POST":
    token = request.form["csrf_token"]
    if user_serv.check_token(token):
      artist = request.form["artist"]
      album_name = request.form["albumname"]
      release_year = request.form["releaseyear"]
      if release_year == "":
        release_year = 0

      genre = request.form["genre"].upper()
      file = request.files["cover_image"]
      if not file.filename.endswith(".jpg"):
        return render_template("addalbum.html", message_image="Invalid file type. Only .jpg files accepted.")
      cover_image = file.read()
      print(len(cover_image), "bytes")
      if len(cover_image) > 1024*1024:
        return render_template("addalbum.html", message_image="Image is too large")
      comment = request.form["comment"]
      grade = int(request.form["grade"])
      songs = []
      songs_length = {}
      song = request.form["song0"]
      if song == "":
        return render_template("addalbum.html", message_song="An album hasto contain atleast one (1) song.")
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
        #return redirect("/album/")
        return redirect("/")
      return render_template("addalbum.html", message_adding=" Adding the new album has failed")
    else:
      return redirect("/")


@app.route("/editalbum", methods=["GET", "POST"])
def edit_album(id:int):
  return redirect("/")


@app.route("/albums", methods=["GET"])
def sort_albums():
  if request.method == "GET":
    sort = request.args.get("sort")
    albums = album_repo.display_albums_asc()
    if sort == "dates_asc":
      albums = album_repo.display_date_asc()
    elif sort == "dates_desc":
      albums = album_repo.display_date_desc()
    elif sort == "albums_asc":
      albums = album_repo.display_albums_asc()
    elif sort == "albums_desc":
      albums = album_repo.display_albums_desc()
    elif sort == "artists_asc":
      albums = album_repo.display_artists_asc()
    elif sort == "artists_desc":
      albums = album_repo.display_artists_desc()
    elif sort == "grades_asc":
      albums = album_repo.display_rating_asc()
    elif sort == "grades_desc":
      albums = album_repo.display_rating_desc()
    images = encode_images_in_albums(albums)
    return render_template("albums.html", albums=albums, images=images, len=len(albums))
    

@app.route("/addreview")#, methods="POST")
def addreview():
  #comment = request.form("comment")
  #grade = request.form("grade")
  return redirect("/")


@app.route("/album/<int:album_id>", methods=["GET", "POST"])
def album(album_id:int):
  if request.method == "GET":
    album_content = album_repo.get_album_by_id(album_id)
    cover_image = image_repo.get_cover_image(album_id)
    song_content = song_repo.get_songs_by_album_id(album_id)
    reviews_content = review_repo.get_reviews_by_id(album_id)
    thumbs = thumb_repo.get_thumbs_for_songs(album_id)
    return render_template("album.html", album=album_content, \
                            cover_image=cover_image, songs=song_content, \
                            reviews=reviews_content, thumbs=thumbs, \
                            songs_len=len(song_content))

  elif request.method == "POST":
    token = request.form["csrf_token"]
    if user_serv.check_token(token):
      comment = request.form["comment"]
      if len(comment) > 5000:
        return render_template("album.html", message_comment=" Review cannot be longer than five thousand (5000) characters.")
      grade = request.form["grade"]
      review_repo.add_review(comment, grade, user_serv.user_id(), album_id)
      return redirect("/album/"+str(album_id))
  return redirect("/")


@app.route("/thumb", methods=["POST"])
def thumb():
  if request.method == "POST":
    token = request.form["csrf_token"]
    if user_serv.check_token(token):
      thumb = request.form["thumb"]
      song_id = request.form["song_id"]
      user_id = request.form["user_id"]
      album_id = request.form["album_id"]
      thumb_repo.add_thumb(song_id, user_id, thumb)
  return redirect("/album/"+str(album_id))


@app.route("/artist/<string:artist_name>", methods=["GET"])
def artist(artist_name:str):
  if request.method == "GET":
    albums = album_repo.get_albums_by_artist_name(artist_name)
    images = encode_images_in_albums(albums)
    return render_template("artist.html", artist_name=artist_name, 
                            albums=albums, images=images, len=len(albums))
  return redirect("/")


@app.route("/admin", methods=["GET", "POST"])
def admin():
  if session["admin"]:
    if request.method == "GET":
      users = user_repo.get_all_users()
      return render_template("admin.html", users=users)
      
    elif request.method == "POST" :
      username = request.form["user"]
      if len(username) == 0:
        users = user_repo.get_all_users()
        return render_template("admin.html", users=users, message_none_found="No users were found by that name.")
      else:
        users = user_repo.get_user_by_name(username)
        return render_template("admin.html", users=users)
  else:
    return redirect("/")  


@app.route("/toggle/admin", methods=["POST"])
def toggle_admin():
  token = request.form["csrf_token"]
  if request.method == "POST" and user_serv.check_token(token) \
     and session["admin"]:
    user_id = request.form["user_id"]
    status = request.form["admin"]
    if status:
      user_repo.promote_user_to_admin(user_id)
    else:
      user_repo.demote_user_from_admin(user_id)
    users = user_repo.get_all_users()
    return render_template("admin.html", users=users)
  return redirect("/")


@app.route("/toggle/hide/song", methods=["POST"])
def toggle_hide_song():
  token = request.form["csrf_token"]
  if request.method == "POST" and user_serv.check_token(token) \
     and session["admin"]:
    album_id = request.form["album_id"]
    song_id = request.form["song_id"]
    status = request.form["visible"]
    status = request.args.get("visible", type=bool)
    if status:
      song_repo.set_song_invisible(song_id)
    else:
      song_repo.set_song_visible(song_id)
    return redirect("/album/"+str(album_id))
  return redirect("/")

def encode_images_in_albums(albums_data):
  encoded_images = []
  for image in albums_data:
    modified_image  = image.cover_img
    modified_image = b64encode(modified_image).decode('utf-8')
    encoded_images.append(modified_image)
  return encoded_images