import sqlite3

from constants import DB_FILE

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Plants
c.execute("""
  INSERT INTO plant VALUES(NULL, 'Spider Plant 1', 'IMG_1671.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Spider Plant 2', 'IMG_1676.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Philodendron 1', 'IMG_1675.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Philodendron 2', 'IMG_1678.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Pilea 1', 'IMG_1672.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Pilea 2', 'IMG_1680.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Rubber Tree', 'IMG_1674.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Peace Lily', 'IMG_1677.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Succulents', 'IMG_1681.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Money Tree', 'IMG_1679.jpeg');
""")

c.execute("""
  INSERT INTO plant VALUES(NULL, 'Propagation Tubes', 'IMG_1673.jpeg');
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