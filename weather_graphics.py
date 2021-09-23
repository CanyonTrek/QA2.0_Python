#! /bin/python
# Create a visual display for our weather data
# Name:        QA2.0, Sarah Chacko
# Revision:    v1.0
# Description:  Use seaborn library  to create some graphs.
#
# Retrieve weather data from the database
#

import seaborn as sns
import matplotlib.pyplot as plt

import weather_db as wd

db = wd.Weather_db()
rows =db.query_and_return('weather')
# rows of tuples - would it be better as dicts?
# We could plot a barchart for cities - temperature or humidity
# or a line graph of data over time
# or a scatter plot ....
# example - temp is the 6th item in each tuple, and is in Kelvin
# opportunity for lambda to convert, and list comprehension
# to get the items?

temps = [row[5] for row in rows]

print(temps)

#sns.lineplot(x=range(len(temps)), y=temps)
cities = [ row[1] for row in rows]
c_temps = [t - 273.15 for t in temps ]
p= sns.barplot(x=cities, y =c_temps, )
p.set_xlabel("City", fontsize = 20)
p.set_ylabel("Temperature (C)", fontsize = 20)
plt.show()

