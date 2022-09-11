from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db
import secrets

def user_id():
  return session.get("user_id", 0)


def check_token(token):
  return session["csrf_token"] == token


def register(username:str, password:str):
  print("register")
  try:
    hash_value = generate_password_hash(password)
    values = {"username":username, "passwrd":hash_value, "is_admin":False}

    sql = "INSERT INTO users (username, passwrd, is_admin) " \
          "VALUES (:username, :passwrd, :is_admin)"
    #db.session.execute(sql, {"username":username, "passwrd":hash_value, "is_admin":a})
    db.session.execute(sql, values)
    db.session.commit()    
  except:
    return False
  return login(username, password)


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
      session["user_id"] = user.id
      session["username"] = username
      session["admin"] = user.is_admin
      session["csrf_token"] = secrets.token_hex(16)
      
      return True
    else:
      return False


def logout():
  del session["username"]
  #del session["admin"]

  session.clear()