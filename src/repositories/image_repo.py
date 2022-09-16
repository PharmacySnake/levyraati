from db import db

def add_cover_image(cover_image, album_id:int):
  values = {"cover_img":cover_image, "album_id":album_id, "visible":True}
  sql = "INSERT INTO images (cover_img, album_id, visible)"\
        "VALUES (:cover_img, :album_id, :visible"
  db.session.execute(sql, values)
  db.session.commit()

def change_cover_image(image_id:int, cover_image):
  print("change cover image")

def remove_cover_image(image_id:int):
  print("remove cover image")

def change_visibility(image_id:int):
  print("change cover visibility")