from db import db


def add_review(comment:str, grade:int, user_id:int, album_id:int):
  values = {"comment":comment, "grade":grade,
            "user_id":user_id, "album_id":album_id, 
            "visible":True}
  sql = "INSERT INTO reviews (comment, grade, date_added, user_id, album_id, visible) "\
        "VALUES (:comment, :grade, NOW(), :user_id, :album_id, :visible)"
  db.session.execute(sql, values)
  db.session.commit()

def get_reviews_by_id(album_id:int):
  sql = "SELECT U.username, R.comment, R.grade " \
        "FROM reviews R " \
        "LEFT JOIN users U ON R.user_id = U.id " \
        "WHERE R.album_id=:album_id"
        #"ORDER BY date" MISSING from database
  result = db.session.execute(sql, {"album_id":album_id})
  return result.fetchall()


def edit_comment(comment:str, album_id:int):
  print("edit comment")


def change_grade(grade:int, album_id:int):
  print("change grade")