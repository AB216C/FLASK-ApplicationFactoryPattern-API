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

# API CRUD Endpoints

.dump() → Marshmallow converts the object(s) to Python-native data types (dicts, lists).

.jsonify() → Flask converts Python dicts/lists to a JSON HTTP response.

setattr(member, field, value) allows us to loop through all the fields and values of our member_data dictionary and update the member.