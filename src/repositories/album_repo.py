from db import db
from sqlalchemy.sql import text
import services.user_serv as user_serv
from repositories import image_repo, review_repo, song_repo


def add_album(artist:str, album_name:str, release_year:int, genre:str, comment:str,
            cover_image, songs:list, songs_length:dict, grade:int):
    user_id = user_serv.user_id()
    if user_id == 0:
        return False

    values = {"user_id":user_id, "artist":artist,
            "album_name":album_name, "release_year":release_year,
            "genre":genre, "editable":True, "visible":True}

    sql = "INSERT INTO albums (user_id, date_added, artist, album_name, release_year, genre, editable, visible) "\
          "VALUES (:user_id, NOW(), :artist, :album_name, :release_year, :genre, :editable, :visible) "\
          "RETURNING id"
    result = db.session.execute(sql, values)
    db.session.commit()
    album_id = result.fetchone()[0]
    if len(cover_image) > 0:
      image_repo.add_cover_image(cover_image, album_id)
    if len(songs) > 0:
      song_repo.add_songs(songs, songs_length, album_id)
    review_repo.add_review(comment, grade, user_id, album_id)
    return True

def get_album_by_id(album_id:int):
  sql = "SELECT A.id, A.user_id, A.date_added, A.artist, A.album_name, " \
               "A.release_year, A.genre " \
        "FROM albums A " \
        "WHERE A.id=:album_id"
  result = db.session.execute(sql, {"album_id":album_id})
  return result.fetchone()
  #return result.fetchall()

def get_albums_by_artist_name(artist_name:str):
  sql = "SELECT A.id, A.artist, A.album_name, A.release_year, " \
               "A.genre, I.cover_img " \
        "FROM albums A " \
        "LEFT JOIN Images I ON A.id = I.album_id " \
        "WHERE artist=:artist_name " \
        "GROUP BY A.id, A.user_id, A.date_added, A.artist, A.album_name, " \
                 "A.release_year, A.genre, I.cover_img " \
        "ORDER BY A.release_year"
  result = db.session.execute(sql, {"artist_name":artist_name})
  return result.fetchall()


def display_albums_home():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.date_added DESC " \
        "LIMIT 10"
  result = db.session.execute(sql)
  return result.fetchall()


def display_albums_desc():
  sql = sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.album_name DESC"
  result = db.session.execute(sql)
  return result.fetchall()


def display_albums_asc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.album_name"
  result = db.session.execute(sql)
  return result.fetchall()


def display_artists_desc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.artist DESC"
  result = db.session.execute(sql)
  return result.fetchall()


def display_artists_asc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.artist"
  result = db.session.execute(sql)
  return result.fetchall()


def display_date_desc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.date_added DESC"
  result = db.session.execute(sql)
  return result.fetchall()


def display_date_asc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
	      "ORDER BY A.date_added"
  result = db.session.execute(sql)
  return result.fetchall()


def display_rating_desc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
        "ORDER BY AVG(R.grade) DESC"
  result = db.session.execute(sql)
  return result.fetchall()


def display_rating_asc():
  sql = "SELECT U.username, A.date_added, A.album_name, A.artist, " \
               "I.cover_img, CAST(AVG(R.grade)*2 AS INTEGER) AS grade, " \
               "A.id AS album_id " \
	      "FROM reviews R " \
	      "LEFT JOIN albums A ON A.id = R.album_id " \
	      "LEFT JOIN users U ON A.user_id = U.id " \
	      "LEFT JOIN images I ON A.id = I.album_id " \
	      "GROUP BY A.album_name, A.artist, U.username, A.date_added, " \
                 "I.cover_img, A.id " \
        "ORDER BY AVG(R.grade)"
  result = db.session.execute(sql)
  return result.fetchall()


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


def toggle_album_editability(album_id:int):
  if album_exists(album_id):
    editable = not get_album_editability(album_id)
    sql = "UPDATE albums SET editable=:editable WHERE id=:album_id"
    db.session.execute(sql, {"editable":editable, "album_id":album_id})
    db.session.commit()
    return True
  return False


def toggle_album_visibility(album_id:int):
  if album_exists(album_id):
    visible = not get_album_visibility(album_id)
    sql = "UPDATE albums SET visible=:visible WHERE id=:album_id"
    db.session.execute(sql, {"visible":visible, "album_id":album_id})
    db.session.commit()
    return True
  return False


def get_album_visibility(album_id:int):
  sql = "SELECT visible FROM albums WHERE id=:album_id"
  result = db.session.execute(sql, {"album_id":album_id})
  return result.fetchone()


def get_album_editability(album_id:int):
  sql = "SELECT editable FROM albums WHERE id=:album_id"
  result = db.session.execute(sql, {"album_id":album_id})
  return result.fetchone()


def album_exists(album_id):
  sql = "SELECT id FROM albums WHERE id=:album_id"
  result = db.session.execute(sql, {"album_id":album_id})
  if not result:
    return False
  return True


