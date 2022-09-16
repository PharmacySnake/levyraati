  CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    passwrd TEXT,
    is_admin BOOLEAN
  );


  CREATE TABLE Albums (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    date_added DATE,
    artist TEXT,
    album_name TEXT,
    release_year INTEGER,
    genre TEXT,
    editable BOOLEAN,
    visible BOOLEAN
  );


  CREATE TABLE Songs (
    id SERIAL PRIMARY KEY,
    song_name TEXT,
    song_len_min INTEGER,
    song_len_sec INTEGER,
    album_id INTEGER REFERENCES Albums,
    visible BOOLEAN
  );


  CREATE TABLE Images (
    id SERIAL PRIMARY KEY,
    cover_img BYTEA,
    album_id INTEGER REFERENCES Albums,
    visible BOOLEAN
  );


  CREATE TABLE Review (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    album_id INTEGER REFERENCES Albums,
    comment TEXT,
    grade INTEGER,
    visible BOOLEAN
  );


  CREATE TABLE Thumbs (
    id SERIAL PRIMARY KEY,
    song_id INTEGER REFERENCES Songs,
    user_id INTEGER REFERENCES Users,
    thumb BOOLEAN
  );