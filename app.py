import sqlite3

from datetime import datetime, timezone
from flask import Flask, jsonify
from db.constants import DB_FILE


app = Flask(__name__)


@app.route('/')
def index():
    return 'Plant Tracker API'


@app.route('/plants')
def plant_waterings():
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
        timestamp = plant['timestamp'];
        if timestamp:
          diff = datetime.now(timezone.utc) - datetime.fromtimestamp(timestamp, timezone.utc)
          plant['last_watered'] = diff.days

    return close_connection_with_response(
        connection,
        dict(plants=response_data),
    )
    

@app.route('/plant/<id>/water', methods=['POST'])
def water_plant(id):
    connection, cursor = open_connection()   
    cursor.execute(    
      f"""
      INSERT INTO watering VALUES(NULL, {id}, {datetime.timestamp(datetime.now(timezone.utc), )});
      """
    )
    connection.commit()

    return close_connection_with_response(
        connection,
        dict(),
    )    
    
    
def open_connection():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = dict_factory
    return con, con.cursor()    


def close_connection_with_response(connection, response_data):
    response = jsonify(response_data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    connection.close()
    return response


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

