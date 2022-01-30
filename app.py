import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy to access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the Flask Dependency
from flask import Flask, jsonify

# # Access the SQLite database.activate pythonData
engine = create_engine("sqlite:///hawaii.sqlite")

# # Reflect the database into our classes.
Base = automap_base()

# # Reflect our tables
Base.prepare(engine, reflect=True)

# # Save our references to each table. Create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# # Create a session link from Python to our database 
session = Session(engine)

# create a Flask application instance called "app"
app = Flask(__name__)


# define the welcome route
@app.route("/")

# Create a function welcome() with a return statement
# Add the precipitation, stations, tobs, and temp routes that we'll need for this module using f-strings
# Naming convention /api/v1.0/ followed by the name of the route signifies that this is version 1 of our application
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

#9.5.3 Precipitation Route

# Create Precipitation Route ---------------------------------------------
@app.route("/api/v1.0/precipitation")

# create the precipitation() function
# calculates the date one year ago from the most recent date in the database
# get the date and precipitation for the previous year
# converts the dictionary to a JSON file
# create a dictionary with the date as the key and the precipitation as the value
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# 9.5.4 Stations Route ------------------------------------------------------

@app.route("/api/v1.0/stations")

# create a new function called stations()
# get all of the stations in our database
# unraveling our results into a one-dimensional array
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# 9.5.5 Monthly Temperature Route ------------------------------------------

@app.route("/api/v1.0/tobs")

# calculate the date one year ago from the last date in the database
# query the primary station for all the temperature observations from the previous year
# unravel the results into a one-dimensional array and convert that array into a list
# jsonify the list and return our results
# jsonify our temps list, and then return it
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# 9.5.6 Statistics Route ------------------------------------------------------

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a function called stats()
# add a start parameter and an end parameter to our stats()function
# create a query to select the minimum, average, and maximum temperatures from our SQLite database
#   by just creating a list called sel
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# to determine the starting and ending date
# query our database using the list that we just made
# unravel the results into a one-dimensional array and convert them to a list
# jsonify our results and return them

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

# the asterisk is used to indicate there will be multiple results for our query: min,avg,max
# calculate the temperature minimum, average, and maximum with the start and end dates
# use the sel list, which is simply the data points we need to collect
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)

# Run:  http://127.0.0.1:5000/api/v1.0/temp/start/end route   ....gives "[null,null,null]" output
# enter any date in the dataset as a start and end date ^
# Let's say we want to find the minimum, maximum, and average temperatures for June 2017
# http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30