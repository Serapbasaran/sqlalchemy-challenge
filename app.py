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
<h1>Hawaii Climate App (Flask API)</h1>
<img src="https://i.ytimg.com/vi/3ZiMvhIO-d4/maxresdefault.jpg" alt="Hawaii Weather"/>
<p>Precipitation Analysis:</p>
<ul>
  <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
</ul>
<p>Station Analysis:</p>
<ul>
  <li><a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
</ul>
<p>Temperature Analysis:</p>
<ul>
  <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
</ul>
<p>Start Day Analysis:</p>
<ul>
  <li><a href="/api/v1.0/2017-03-14">/api/v1.0/2017-03-14</a></li>
</ul>
<p>Start & End Day Analysis:</p>
<ul>
  <li><a href="/api/v1.0/2017-03-14/2017-03-28">/api/v1.0/2017-03-14/2017-03-28</a></li>
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
        


if __name__ == '__main__':
    app.run(debug=True)

