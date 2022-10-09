from db import db

def thumb(song_id:int, user_id:int, value:int):
  values = {"song_id":song_id, "user_id":user_id, "thumb":value}
  sql = "INSERT INTO thumbs (song_id, user_id, thumb) " \
        "VALUES (:song_id, :user_id, :value)"
  db.session.execute(sql, values)
  db.session.commit()
