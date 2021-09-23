#! /bin/python
# Create a visual display for our weather data
# Name:        QA2.0, Sarah Chacko
# Revision:    v1.0
# Description:  Use seaborn library  to create some graphs.
#
# Retrieve weather data from the database
#

import seaborn

import weather_db as wd

rows = wd.Weather_db.query_and_return('weather')



