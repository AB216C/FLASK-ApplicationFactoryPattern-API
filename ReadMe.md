# Establish one to many, and many to many relationship between models


After do the following:

# Installation:

- windows
python -m venv venv

- mac
python3 -m venv venv


# Activating the environment
- windows
venv\Scripts\activate

- mac
source venv/bin/activate


# Installing packages to the environment

- windows 
pip install flask flask-sqlalchemy mysql-connector-python

-mac
pip3 install flask flask-sqlalchemy mysql-connector-python

# Add models


# Add schemas
Flask-Marshmallow Documentation

Marshmallow is a popular library used in Flask applications to serialize and deserialize data, as well as for input data validation. It works well with ORMs like SQLAlchemy but is not limited to them.

Serialization: Converts complex objects (like SQLAlchemy model objects) into simpler data types (like JSON) to send over the network.
Deserialization: Converts raw input data into application-specific data structures, such as populating a SQLAlchemy model.
Validation: Ensures that input data conforms to expected types and formats before processing.


## Installation 
pip3 install flask-marshmallow, marshmallow-sqlalchemy

# API CRUD Endpoints

.dump() → Marshmallow converts the object(s) to Python-native data types (dicts, lists).

.jsonify() → Flask converts Python dicts/lists to a JSON HTTP response.

setattr(member, field, value) allows us to loop through all the fields and values of our member_data dictionary and update the member.