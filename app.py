import sqlite3

from datetime import datetime, timezone
from flask import Flask, jsonify, render_template
from db.constants import DB_FILE


app = Flask(__name__)

@app.route('/')
def index():
    connection, cursor = open_connection()
    res = cursor.execute(
      """
        SELECT plant.id, plant.name, plant.image, watering.timestamp
          FROM plant
          LEFT JOIN (
            SELECT MAX(timestamp), timestamp, plant_id
            FROM watering 
            GROUP BY plant_id       
          ) watering
          ON plant.id = watering.plant_id; 
      """)    
    response_data = res.fetchall();

    for plant in response_data:
        plant['last_water'] = get_last_water_text(plant['timestamp'])   

    connection.close()
    
    return render_template(
        'index.html',
        plants=response_data,
    )

@app.route('/plant/<id>/water', methods=['POST'])
def water_plant(id):
    connection, cursor = open_connection()   
    timestamp = datetime.timestamp(datetime.now(timezone.utc), )
    cursor.execute(    
      f"""
      INSERT INTO watering VALUES(NULL, {id}, {timestamp});
      """
    )
    connection.commit()
    connection.close()

    response = dict(
        id=id,
        last_water=get_last_water_text(timestamp)
    )
    return response


def get_last_water_text(timestamp):
  if timestamp:
    diff = datetime.now(timezone.utc) - datetime.fromtimestamp(timestamp, timezone.utc)
    days = diff.days
    if days == 0:
      return 'Watered Today'
    return f"{days} days ago"
  return 'Never Watered'
    
    
def open_connection():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = dict_factory
    return con, con.cursor()    


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

