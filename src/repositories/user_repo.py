from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from services import user_serv
import secrets


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
      user_serv.set_user(user.id, username, user.is_admin, secrets.token_hex(16))
      #session["user_id"] = user.id
      #session["username"] = username
      #session["admin"] = user.is_admin
      #session["csrf_token"] = secrets.token_hex(16)
      return True
    else:
      return False


