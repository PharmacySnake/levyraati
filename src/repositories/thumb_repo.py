from db import db

def add_thumb(song_id:int, user_id:int, thumb:int):
  values = {"song_id":song_id, "user_id":user_id, "thumb":thumb}
  sql = "INSERT INTO thumbs (song_id, user_id, thumb) " \
        "VALUES (:song_id, :user_id, :thumb)"
  db.session.execute(sql, values)
  db.session.commit()


def get_thumbs_for_songs(album_id:int):
  sql = "SELECT song_id, user_id, " \
        "COUNT(CASE WHEN thumb < 0 THEN -1 ELSE 0 END) AS thum_neg, " \
	      "COUNT(CASE WHEN thumb > 0 THEN 1 ELSE NULL END) AS thum_pos, " \
	      "CAST(AVG(thumb)*5 AS INTEGER) AS thumb " \
	      "FROM thumbs " \
	      "LEFT JOIN songs ON songs.id = song_id " \
	      "WHERE songs.album_id=:album_id " \
	      "GROUP BY song_id, user_id"
        #""" 
	      #SELECT song_id, CAST(AVG(thumb)*5 AS INTEGER) AS thumb, user_id 
	      #FROM thumbs 
	      #LEFT JOIN songs ON songs.id = song_id 
	      #WHERE songs.album_id=:album_id
	      #GROUP BY song_id, user_id
        #"""
  result = db.session.execute(sql, {"album_id":album_id})
  return result.fetchall()

def check_if_user_thumbed(song_id:int, user_id:int, album_id:int):
  values = {"song_id":song_id, "user_id":user_id, "album_id":album_id}
  sql = """ 
        SELECT 
        FROM thumbs
        WHERE 
        """
  return 0