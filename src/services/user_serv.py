from flask import session


def set_user(id:int, username:str, is_admin:bool, token_hex:str):
  session["user_id"] = id
  session["username"] = username
  session["admin"] = is_admin
  session["csrf_token"] = token_hex


def user_id():
  return session.get("user_id", 0)


def check_token(token):
  return session["csrf_token"] == token


def logout():
  del session["username"]
  #del session["admin"]
  session.clear()