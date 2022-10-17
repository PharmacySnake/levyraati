from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from services import user_serv
import secrets


def register(username:str, password:str, admin:bool):
  try:
    hash_value = generate_password_hash(password)
    values = {"username":username, "passwrd":hash_value, "is_admin":admin}

    sql = "INSERT INTO users (username, passwrd, is_admin) " \
          "VALUES (:username, :passwrd, :is_admin)"
    db.session.execute(sql, values)
    db.session.commit()    
  except:
    return False
  return login(username, password)


def check_username_availability(username:str):
  sql = "SELECT username " \
        "FROM users " \
        "WHERE username=:username"
  result = db.session.execute(sql, {"username":username})
  return bool(result.fetchall())


def get_all_users():
  sql = "SELECT * FROM users"
  result = db.session.execute(sql)
  return result.fetchall()

def get_user_by_name(username:str):
  sql = "SELECT * FROM users WHERE usernmame=:username"
  result = db.session.execute(sql, {"username":username})
  return result.fetchone()

def login(username:str, password:str):
  sql = "SELECT id, passwrd, is_admin " \
        "FROM users " \
        "WHERE username=:username"
  result = db.session.execute(sql, {"username":username})
  user = result.fetchone()
  if not user:
    return False
  else:
    if check_password_hash(user.passwrd, password):
      user_serv.set_user(user.id, username, user.is_admin, secrets.token_hex(16))
      return True
    else:
      return False


def promote_user_to_admin(user_id:int):
  if user_exists(user_id):
    sql = "UPDATE users SET is_admin=true where id=:user_id"
    db.session.execute(sql, {"user_id":user_id})
    db.session.commit()
    return True
  return False


def demote_user_from_admin(user_id:int):
  if user_exists(user_id):
    sql = "UPDATE users SET is_admin=false where id=:user_id"
    db.session.execute(sql, {"user_id":user_id})
    db.session.commit()
    return True
  return False


def user_exists(user_id:int):
  sql = "SELECT id FROM users WHERE id=:user_id"
  result = db.session.execute(sql, {"user_id":user_id})
  if not result:
    return False
  return True


