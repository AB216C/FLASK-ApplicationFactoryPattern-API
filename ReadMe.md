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

## APPLICATION FACTORY PATTERN
# The Application Factory Pattern in Flask
What is the Application Factory Pattern?
# Definition:
The Application Factory Pattern is a design pattern used to create and configure instances of an application in a modular and flexible manner. Instead of creating a Flask application object directly at the top level, the application factory pattern involves writing a function that returns a new instance of the application.
# Why Use the Application Factory Pattern?
# Advantages:
Modularity: With the incorporation of blueprints, we are able to create a separation of concerns, and compartmentalize actions and interactions
Scalability: With this increased organization we improve the ability to scale and maintain our API.
Configuration: Allows for different configurations (e.g., for testing, development, and production) without altering the core application code.
Testing: Makes it easier to create multiple instances of the app for testing purposes, as each test can create its own isolated app instance.
Implementing the Application Factory Pattern
# Basic Structure:
create_app(): A function that initializes the Flask application and returns it, located in the application folder's init file
extensions.py: A file used to initialize any other miscellaneous flask extensions (i.e. Flask-Limiter, Flask-cache, etc.)
blueprints: Are collections of related routes that provides organization and separation of concerns
models: This is the folder we create our Models
app.py: Imports our create_app() from application and runs it, instantiating our app
config.py: Holds our configurations to be used in our create_app() configure the app.


## Flask-Limiter


1. Understand Flask-Limiter: Learn how to use rate limiting to protect APIs from abuse, such as excessive traffic or DDOS attacks.
2. Understand Flask-Caching: Use caching to enhance performance by reducing repetitive database queries and improving response times.
3. Implement Flask-Limiter: Set up rate limits at a global or route-specific level in a Flask API using the Application Factory Pattern.
4. Implement Flask-Caching: Apply caching to routes that involve expensive or repetitive data retrieval using Flask-Caching.


# What is Flask-Limiter?
Flask-Limiter is an extension that provides rate limiting to Flask applications, which is essential for preventing abuse by limiting the number of requests a client can make to the API. This allows us to protects our API from malicious attacks like DDOS attacks, which are repetitive requests (100's even 1000's per second) used to overwhelm your server.
Use Cases:


# Protecting routes from excessive traffic
Throttling requests to sensitive endpoints (login, registration, etc.)


# Installing Flask-Limiter


pip install Flask-Limiter


# How Flask-Limiter Works
Flask-Limiter allows you to set limits per route or globally. The rate limit syntax follows a simple format like 5 per minute or 100 per hour.


# Get list of downloaded packages in your folder


pip3 freeze > requirements.txt
