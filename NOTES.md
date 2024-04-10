# Plant Tracker

- Displays list of plants
- Each list item includes
  - Name
  - Image
  - Days since last water
  - Button to Water
- Clicking list item displays detail page
- Detail page includes
  - Name
  - Image
  - Description
  - Lighting Needs
  - Fertilizing Needs
  - Soil Mix
  - Record of waterings

# Specs

- API
  - Flast: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/1
  - Datetime module: https://www.geeksforgeeks.org/python-datetime-module
  - Sqlite: https://docs.python.org/3/library/sqlite3.html
- For Client, piggy back on existing lighthttpd web server
  - /var/www/html/plants

# Misc

```
scp -r ./workspace/plant-tracker/* greg@raspberrypi.local:~/workspace/plant-tracker
```
