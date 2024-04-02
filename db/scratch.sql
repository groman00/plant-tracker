-- Get Plants and Last water date
SELECT plant.id, plant.name, plant.image, watering.timestamp
FROM plant
  LEFT JOIN ( 
    SELECT timestamp, plant_id
  FROM watering
  ORDER BY timestamp LIMIT 1 
  ) watering
  ON plant.id = watering.plant_id ;

