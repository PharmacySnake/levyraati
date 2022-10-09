from db import db

def add_thumb(song_id:int, user_id:int, thumb:int):
  values = {"song_id":song_id, "user_id":user_id, "thumb":thumb}
  sql = "INSERT INTO thumbs (song_id, user_id, thumb) " \
        "VALUES (:song_id, :user_id, :thumb)"
  db.session.execute(sql, values)
  db.session.commit()
