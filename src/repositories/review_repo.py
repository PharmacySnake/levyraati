from db import db


def add_review(comment:str, grade:int, user_id:int, album_id:int):
  values = {"comment":comment, "grade":grade,
            "user_id":user_id, "album_id":album_id, 
            "visible":True}
  sql = "INSERT INTO reviews (comment, grade, album_id, visible) "\
        "VALUES (:comment, :grade, :album_id, :visible)"
  db.session.execute(sql, values)
  db.session.commit()


def edit_comment(comment:str, album_id:int):
  print("edit comment")


def change_grade(grade:int, album_id:int):
  print("change grade")