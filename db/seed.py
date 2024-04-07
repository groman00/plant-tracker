import sqlite3

from constants import DB_FILE

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Plants
c.execute("""
  INSERT INTO plant VALUES(NULL, 'Spider Plant 1', 'image-1.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Spider Plant 2', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Philodendron 1', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Philodendron 2', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Pilea 1', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Pilea 2', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Rubber Tree', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Peace Lily', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Succulents', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Money Tree', 'image-2.jpg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Propagation Tubes', 'image-2.jpg');
""")

# Waterings
# c.execute("""
#   INSERT INTO watering VALUES(NULL, 1, 1711930350);
# """)
# c.execute("""
#   INSERT INTO watering VALUES(NULL, 1, 1706746350);
# """)

conn.commit()
conn.close()