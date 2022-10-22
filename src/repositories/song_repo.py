from db import db


def add_songs(songs:list, song_length:dict, album_id:int):
  for song, key in zip(songs,song_length): 
    if song != "":
      song_name = song
      if key != "":
        song_len_min = key
      else:
        song_len_min = 0
      if song_length[key] != "":
        song_len_sec = song_length[key]
      else:
        song_len_sec = 0

    values = {"song_name":song_name, "song_len_min":song_len_min,
              "song_len_sec":song_len_sec, "album_id":album_id, 
              "visible":True}
    sql = "INSERT INTO songs (song_name, song_len_min, song_len_sec, album_id, visible) "\
          "VALUES (:song_name, :song_len_min, :song_len_sec, :album_id, :visible)"
    db.session.execute(sql, values)
    db.session.commit()

def get_songs_by_album_id(album_id:int):
  sql = "SELECT id, song_name, song_len_min, song_len_sec, visible " \
        "FROM songs " \
        "WHERE album_id=:album_id"
  result = db.session.execute(sql, {"album_id":album_id})
  return result.fetchall()

def change_song_name(song_id:int, name:str):
  print("change song name")


def change_song_length(song_id:int, song_len_min:int, song_len_sec:int):
  print("change song length")


def remove_song(song_id:int):
  print("remove song")


def set_song_visible(song_id:int):
  if song_exists(song_id):
    sql = "UPDATE songs SET visible=false WHERE id=:song_id"
    db.session.execute(sql, {"song_id":song_id})
    db.session.commit()
    return True
  return False

def set_song_visible(song_id:int):
  if song_exists(song_id):
    sql = "UPDATE songs SET visible=false WHERE id=:song_id"
    db.session.execute(sql, {"song_id":song_id})
    db.session.commit()
    return True
  return False

def song_exists(song_id):
  sql = "SELECT id FROM songs WHERE id=:song_id"
  result = db.session.execute(sql, {"song_id":song_id})
  if not result:
    return False
  return True