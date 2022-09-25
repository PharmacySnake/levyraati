from base64 import b64encode
from db import db
from flask import make_response


def add_cover_image(cover_image, album_id:int):
  #print(cover_image)
  #print(3)
  values = {"cover_img":cover_image, "album_id":album_id,
            "visible":True}
  sql = "INSERT INTO images (cover_img, album_id, visible) " \
        "VALUES (:cover_img, :album_id, :visible)"
  db.session.execute(sql, values)
  db.session.commit()


def get_cover_image(album_id:int):
  sql = "SELECT cover_img " \
        "FROM images " \
        "WHERE album_id=:album_id"
  result = db.session.execute(sql, {"album_id":album_id})
  data = result.fetchone()[0]
  cover_image = b64encode(data).decode('utf-8')
  return cover_image

def change_cover_image(image_id:int, cover_image):
  print("change cover image")


def remove_cover_image(image_id:int):
  print("remove cover image")


def change_visibility(image_id:int):
  print("change cover visibility")