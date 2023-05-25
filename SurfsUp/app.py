# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta

from flask import Flask, jsonify

#################################################
# Database Setup

#################################################

# create engine to connect to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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

# Define the homepage route
@app.route('/')
def home():
    """Homepage."""
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

# Define the precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    """Precipitation route."""
    # Calculate the date one year ago from today
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Perform the precipitation query and convert the results to a dictionary
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precipitation_dict = {date: prcp for date, prcp in results}

    session.close()
    
    # Return the JSON representation of the dictionary
    return jsonify(precipitation_dict)


# Define the stations route
@app.route('/api/v1.0/stations')
def stations():
    """Stations route."""
    # Perform the stations query
    results = session.query(Station.station).all()
    stations_list = list(np.ravel(results))
    
    session.close()
    
    # Return the JSON representation of the list
    return jsonify(stations_list)


# Define the tobs route
@app.route('/api/v1.0/tobs')
def tobs():
    """Temperature Observations route."""
    
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Perform the temperature observations query for the most active station
    results = session.query(Measurement.date, Measurement.tobs) \
        .filter(Measurement.station == "USC00519281").filter(Measurement.date >= prev_year).all()
    
    # Create a list of dictionaries containing date and temperature observations
    tobs_list = []
    for date, tobs in results:
        tobs_list.append({'date': date, 'tobs': tobs})
    
    session.close()
    
        # Return the JSON representation of the list
    return jsonify(tobs_list)
        
        
@app.route('/api/v1.0/<start>')
def calc_temps_start(start):
    # Perform query to calculate TMIN, TAVG, and TMAX for dates greater than or equal to start
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
        .filter(Measurement.date >= start).all()
    
    session.close()
        
# Create a dictionary to store the query results
    temperatures = {'TMIN': results[0][0], 'TAVG': results[0][1], 'TMAX': results[0][2]}
    
# Convert the dictionary to a JSON response object
    return jsonify(temperatures)


@app.route('/api/v1.0/<start>/<end>')
def calc_temps_start_end(start, end):
   # Perform query to calculate TMIN, TAVG, and TMAX for the date range from start to end (inclusive)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
        .filter(Measurement.date >= start) \
        .filter(Measurement.date <= end) \
        .all()
    
    session.close()
        
# Create a dictionary to store the query results
    temperatures = {'TMIN': results[0][0], 'TAVG': results[0][1], 'TMAX': results[0][2]}
    
# Convert the dictionary to a JSON response object
    return jsonify(temperatures)


# Run the Flask app

if __name__ == '__main__':
    app.run(debug=True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



