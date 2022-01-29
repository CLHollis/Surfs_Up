import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy to access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the Flask Dependency
from flask import Flaskpython, jasonify

# # Access the SQLite database.
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

# Create Precipitation Route
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


   # http://127.0.0.1:5000/api/v1.0/precipitation

# 9.5.4 Stations Route

@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)