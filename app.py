import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
app = Flask(__name__)

#################################################
# Flask Routes

# Main homepage route
@app.route("/")
def main():
    "List all available routes"
    return(
        f"Welcome to the Climate App Home Page!<br>"
        f"<br>Available routes:<br>"
        f"<br>Precipitation over the last 12 months: /api/v1.0/precipitation<br>"
        f"List of Stations: /api/v1.0/stations<br>"
        f"Temperature at the most active station over the last 12 months: /api/v1.0/tobs<br>"
        f"Temperature statistics from the start date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature statistics from start to end dates(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    sel = [measurement.date, measurement.prcp]
    query = session.query(*sel).\
        filter(measurement.date > '2016-08-22').\
        filter(measurement.date <= '2017-08-23').\
        order_by(measurement.date).all()

    session.close()

    # Convert query results into dictionary and jsonify for user
    results = dict(query)
    return jsonify(results)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    sel = [station.name, station.station]
    query = session.query(*sel).\
        order_by(station.name).all()
    
    session.close()

    # Convert query results into dictionary and jsonify for user
    results = dict(query)
    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    sel = [measurement.date, measurement.tobs]
    query = session.query(*sel).\
        filter(measurement.date > '2016-08-22').\
        filter(measurement.date <= '2017-08-23').\
        filter(measurement.station == "USC00519281").\
        order_by(measurement.date).all()

    session.close()

    # Convert query results into dictionary and jsonify for user
    results = dict(query)
    return jsonify(results)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
    
    # Go through If statement if no end date given
    if not end:
        query = session.query(*sel).\
            filter(measurement.date >= start).all()

        session.close()

        results = []
        for min, max, avg in query:
            tobs_dict = {}
            tobs_dict["Min Temp"] = min
            tobs_dict["Max Temp"] = max
            tobs_dict["Average Temp"] = round(avg, 2)
            results.append(tobs_dict)

        return jsonify(results)

    # Else run the following with end date
    else:
        query = session.query(*sel).\
            filter(measurement.date >= start).\
            filter(measurement.date <= end).all()

        session.close()

        results = []
        for min, max, avg in query:
            tobs_dict = {}
            tobs_dict["Min Temp"] = min
            tobs_dict["Max Temp"] = max
            tobs_dict["Average Temp"] = round(avg, 2)
            results.append(tobs_dict)
        return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)