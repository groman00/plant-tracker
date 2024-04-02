import sqlite3

from constants import DB_FILE

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Plants
c.execute("""
  INSERT INTO plant VALUES(NULL, 'test-plant-1', 'image-1.jpg');
""")
c.execute("""
  INSERT INTO plant VALUES(NULL, 'test-plant-2', 'image-2.jpg');
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