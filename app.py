import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False}, echo=True)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Home Route
@app.route("/")
def welcome():
        return """<html>
    <h1>Hawaii Wheater App </h1>
<img src="https://s3-us-east-2.amazonaws.com/orbitz-media/blog/wp-content/uploads/2014/07/16152729/coconutPIXLR.jpg" >

<p> List of precipitation data for the last year of dataset</p>

<ul>
  <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
</ul>

<p>List of the stations in the dataset</p>

<ul>
  <li><a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
</ul>

<p>The dates and temperature observations of the most active station for the last year of data</p>

<ul>
  <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
</ul>
<p>List of the minimum temperature, the average temperature, and the max temperature for the days greater and equal to start day</p>
<ul>
  <li><a href="/api/v1.0/start">/api/v1.0/start</a></li>
</ul>
<p>List of the minimum temperature, the average temperature, and the max temperature for between start and end day</p>
<ul>
  <li><a href="/api/v1.0/start-end">/api/v1.0/start-end</a></li>
</ul>
</html>
"""
@app.route("/api/v1.0/precipitation")
def precipitation():
   # Design a query to retrieve the last 12 months of precipitation data and plot the results

   # Get the last date in the measurement table
     last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

   # Calculate the date 1 year ago from the last data point in the database
     date_oneyear_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

   # Perform a query to retrieve the data and precipitation scores
     prcp_query = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= date_oneyear_ago).\
     order_by(Measurement.date).all()

    # Convert list of tuples into normal list
     precipitation_dict = dict(prcp_query)
        
    # Return JSON files to Dictionary
     return jsonify(precipitation_dict)
        
@app.route("/api/v1.0/stations")
def stations():
    #design a query to get the list of the stations in database
    stations= session.query(Station.station, Station.name).all()
    # Convert List of Tuples Into Normal List
    station_list = dict(stations)
    # Return JSON List of Stations from the Dataset
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    #Query the dates temperature observations of the most active station for the last year of data
    date_oneyear_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    
    observation_data = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= date_oneyear_ago).\
    filter(Measurement.station == "USC00519281").\
    order_by(Measurement.date).all()
    
    # Convert list of tuples into normal list
    observation = dict(observation_data)
        
    # Return JSON files to Dictionary
    return jsonify(observation)

@app.route("/api/v1.0/start")
def start():
    #When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date
    date = "2017-05-14"      
    data = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= date).\
    group_by(Measurement.date).all()
    temp_list = list(data)
        
    # Return JSON files to Dictionary
    return jsonify(temp_list)

@app.route("/api/v1.0/start-end")
def start_end():
    #When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date
    start_date = "2017-05-14"     
    end_date = "2017-05-28"
    data = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).\
    filter(Measurement.date<= end_date).\
    group_by(Measurement.date).all()
    temp_list = list(data)
        
    # Return JSON files to Dictionary
    return jsonify(temp_list)


if __name__ == '__main__':
    app.run(debug=True)

