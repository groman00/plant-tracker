
-- Get plants with most recent watering.
SELECT plant.id, plant.name, plant.image, watering.timestamp
FROM plant
  LEFT JOIN (
    SELECT MAX(timestamp), timestamp, plant_id
  FROM watering
  GROUP BY plant_id       
  ) watering
  ON plant.id = watering.plant_id; 