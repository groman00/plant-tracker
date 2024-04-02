import sqlite3

from constants import DB_FILE

con = sqlite3.connect(DB_FILE)
cur = con.cursor()
cur.execute(
  """
    CREATE TABLE plant(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT, 
      image TEXT
    )
  """)
cur.execute(
  """
  CREATE TABLE watering(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_id INTEGER, 
    timestamp INTEGER,
    FOREIGN KEY(plant_id) REFERENCES plant(id)
  )
  """
)
