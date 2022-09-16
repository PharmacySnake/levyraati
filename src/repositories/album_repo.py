from datetime import datetime
from db import db
import services.user_serv as user_serv
from repositories import image_repo, song_repo


def add_album(artist:str, album_name:str, release_year:int, genre:str, comment:str,
            cover_image:int, songs:list, songs_length:dict, grade:int):
    user_id = user_serv.user_id()
    if user_id == 0:
        return False

    print("alpumin tekkoon")
    date_added = str(datetime.now())
    values = {"user_id":user_id, "date_added":date_added,
            "artist":artist, "album_name":album_name,
            "release_year":release_year, "genre":genre,
            "editable":True, "visible":True}

    sql = "INSERT INTO albums (user_id, date_added, artist, album_name, release_year, genre, editable, visible) "\
          "VALUES (:user_id, :date_added, :artist, :album_name, :release_year, :genre, :editable, :visible) "\
          "RETURNING id"
    result = db.session.execute(sql, values)
    db.session.commit()
    print("tehtynnä")
    album_id = result.fetchone()[0]
    if len(cover_image) > 0:
      image_repo.add_cover_image(cover_image, album_id)
    if len(songs) > 0:
      song_repo.add_songs(songs, songs_length, album_id)
    return True


def change_album_name(album_id:int, album_name:str):
	print("change album name")


def change_album_artist(album_id:int, artist:str):
	print("change album artist")


def change_album_release(album_id:int, release:int):
	print("change album release")


def change_album_genre(album_id:int, genre:str):
	print("change album genre")


def remove_album(album_id:int):
	print("remove album")


def get_album_length(album_id:int):
	print("get album length")


def change_visibility(album_id:int):
  print("change album visibility")
"""
      date_now = date.today()
      artist = request.form("artist")
      album_name = request.form("albumname")
      release_year = request.form("releaseyear")
      genre = request.form("genre").upper()
      cover_image = request.form("cover_image")
      comment = request.form("comment")
      grade = request.form("grade")
      songs = request.form("songs")

"""