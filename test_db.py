import sys

sys.path.append(r"C:\labs\projects\QA2_python")

import weather_db
data = weather_db.Weather_db()

print(data)
data.create_table()

data.insert_row(table_name="weather", city="glasgow", country="uk", wind_direction="N", temp=100)
data.insert_row(table_name="weather", city="london", humidity=56.6, country="uk", wind_direction="SE", temp=20)

data.query_all()
