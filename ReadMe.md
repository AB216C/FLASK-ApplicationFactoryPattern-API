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

# Special Installation

# Start with:



python3 -m venv path/to/venv
source path/to/venv/bin/activate

python3 -m pip install Flask-Limiter

# Packages:
python3 -m pip install xyz

python3 -m pip install flask_marshmallow

python3 -m pip install flask_sqlalchemy

python3 -m pip install marshmallow-sqlalchemy

python3 -m pip install mysql-connector-python

python3 -m pip install Flask-Caching

python3 -m pip install Flask-Limiter


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

pip3 install Flask-Limiter --break-system-packages    //Not easy to install without breaking homebrew package

python3 -m pip install Flask-Limiter

# How Flask-Limiter Works
Flask-Limiter allows you to set limits per route or globally. The rate limit syntax follows a simple format like 5 per minute or 100 per hour.

# What is Flask-Caching?
Flask-Caching is an extension to cache data and improve performance in Flask applications by storing the results of expensive or frequently accessed API calls. By storing frequently accessed data to a cache, when that data is requested you can simply reach into the cache for the information, instead of performing a full database query. This increases the speed at which the data is returned and also prevents repetitive calls to the db.

# Use Cases:

Caching API responses to reduce database queries
Improving response times for high-traffic endpoints
# Get list of downloaded packages in your folder

pip3 freeze > requirements.txt

pip3 install Flask-Caching --break-system-packages

python3 -m pip install Flask-Caching 

# Start with:

python3 -m venv path/to/venv

source path/to/venv/bin/activate

# Packages:
python3 -m pip install xyz

python3 -m pip install flask_marshmallow

python3 -m pip install flask_sqlalchemy

python3 -m pip install marshmallow-sqlalchemy

python3 -m pip install mysql-connector-python


python3 -m pip install python-jose  #To handle authentication

# Documentation
https://flask-limiter.readthedocs.io/en/stable/

https://flask-caching.readthedocs.io/en/latest/

# Introduction to Token Authentication
What is Token Authentication?
Token authentication is a security mechanism where a server issues a token (a string) to a client after successful authentication. The client uses this token to authenticate subsequent requests.
# Why use Token Authentication?

It’s stateless: no need to store user session data on the server.
Commonly used in modern APIs, especially with single-page applications (SPAs) and mobile apps.

# Token-Based Authentication Flow
Send a POST request to server to authenticate: The client sends a POST request with user credentials (email/username and password).
Verify Credentials: The server checks if credentials are valid.
Create Token: If valid, the server encodes a token with user details.
Send Token to Client: The server sends the token back to the client.
Send Token to Resources that required Token auth: The client sends the Token to access resources.
Verify Token: The resource server verifies the Token's authenticity.
Access Granted: If valid, the server grants access, and the route function runs.
Access Denied: If invalid, access is denied.

# Example on Implementing Token Authentication in Flask
# Project Structure

Here’s the project structure, including a new utils/ folder for utility functions.

/project
├── /application
│   ├── __init__.py - create_app() lives here
│   ├── extensions.py
│   ├── /blueprints
│		│		├──/user
│		│				├──__init__.py  - Initializt User Blueprint
│		│				├── routes.py  - Create User Controllers/routes
│		│				└── userSchemas.py
│   ├── /utils  # <---     New Folder
│		│	        └── util.py #<---   File for token functions
│   └── models.py
├── app.py
└── config.py


# Creating the encode_token Function to generate JWTs.


What is JWT (JSON Web Token)?
JWT is a compact, URL-safe token format that is digitally signed. It contains three parts:

Header: Specifies the type of token and the algorithm used.
Payload: Contains claims such as user data (This makes the tokens user specific).
Signature: Ensures the token hasn’t been altered.

# app/utils/util.py
from datetime import datetime, timedelta, timezone
from jose import jwt
import jose

SECRET_KEY = "a super secret, secret key"

def encode_token(user_id): #using unique pieces of info to make our tokens user specific
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=0,hours=1), #Setting the expiration time to an hour past now
        'iat': datetime.now(timezone.utc), #Issued at
        'sub':  str(user_id) #This needs to be a string or the token will be malformed and won't be able to be decoded.
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Explanation:

The token will expire after 0 days and 1 Hour (exp).
iat is the time the token is "issued at".
The sub claim (subject) contains the user’s ID which needs to be converted to a string.
HS256 is a hashing algorithm to encode the token
SECRET_KEY is a key specific to your application used to "sign" tokens. When validating tokens we look for this signature to ensure that the token is authentic. This prevents forgery of tokens.
Disclaimer:
When creating the payload it is import to follow the same naming convention for the dictionary keys "exp", "iat", "sub". Not only are these keys apart of standard token naming convention, but some of the built-in token validators require these as well and changing them can lead to errors.

Creating login route that grants the user a token
In the user blueprint
# app/blueprints/user/routes
from flask import jsonify
from app.blueprints.user import user_bp
from app.models import User
from app.extensions import limiter
from .schemas import user_schema, users_schema
from app.utils.util import encode_token

@user_bp.route("/login", methods=['POST']
def login():
    try:
        credentials = request.json
        username = credentails['email']
				password = credentials['password']
    except KeyError:
        return jsonify({'messages': 'Invalid payload, expecting username and password'}), 400
    
    query =select(User).where(User.email == email) 
    user = db.session.execute(query).scalar_one_or_none() #Query user table for a user with this email

    if user and user.password == password: #if we have a user associated with the username, validate the password
        auth_token = encode_token(user.id, user.role.role_name)

        response = {
            "status": "success",
            "message": "Successfully Logged In",
            "auth_token": auth_token
        }
        return jsonify(response), 200
    else:
        return jsonify({'messages': "Invalid email or password"}), 401
Explanation:
Import encode_token() onto user blueprint.
The client will POST login credentials {"email": "example@email.com", "password": "password"} to users/login.
The email is then used to query the database for a user
If we find a user with that email, and the password for that user is the same as the password passed in, we will encode a token using encode_token() and return it to the user.
Creating the token_required Decorator
What is a Decorator in Python?

A decorator is a function that wraps around another function, adding functionality to it without modifying the original function. You can Identify decorators by the @ symbol. ex: @decorator

Writing the token_required Decorator
This decorator will be applied to protected routes to ensure that a valid token is present in the request headers.

# app/utils/util.py
from functools import wraps
from flask import request, jsonify


SECRET_KEY = "a super secret, secret key"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Look for the token in the Authorization header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # Decode the token
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = data['sub']  # Fetch the user ID
            
        except jose.exceptions.ExpiredSignatureError:
             return jsonify({'message': 'Token has expired!'}), 401
        except jose.exceptions.JWTError:
             return jsonify({'message': 'Invalid token!'}), 401

        return f(user_id, *args, **kwargs)

    return decorated

# Explanation:

We ensure that the user is making a request with the 'Authorization' field in the request headers
The token is extracted from the Authorization header (Bearer <token>).
If no token is found, a 401 (Unauthorized) response is returned.
The token is decoded using the same secret key that was used to encode it
When we decode the token it produces the same payload that was used to encode the token, including exp, iat, and sub
Accessing sub from the decoded data returns the user_id
If the token is expired or invalid, an appropriate error message is returned.
If everything succeeds the wrapped function is free to run, and the user_id is passed to the wrapped function
Applying Token Authentication to Routes
Modifying the user Blueprint
Now that the token-related functions are in place, we can protect certain routes using the token_required decorator.

# app/blueprints/user/routes
from flask import jsonify
from app.blueprints.user import user_bp
from app.models import User
from app.extensions import limiter
from .schemas import user_schema, users_schema
from app.utils.util import encode_token, token_required

@user_bp.route("/login", methods=['POST']
def login():
	    #login route logic from above
	
	
@user_bp.route('/', methods=['DELETE'])
@token_rquired
def delete_user(user_id): #Recieving user_id from the token
    query = select(User).where(User.id == user_id)
    user = db.session.execute(query).scalars().first()
		
		db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"succesfully deleted user {user_id}"})

# Explanation:
Import token_required onto the user blueprint.
The /login route simulates a login by issuing a token.
We add the @token_required wrapper to the DELETE user route, so now a user needs to be logged in to be able to delete their account.
Notice the change to the endpoint. It is no longer a dynamic route that has /<int:user_id> attached, this is because we get the users id from the token, and @token_required passes that id to delete_user().



RateLimiting-Caching-TokenAuthentication % python3 -m pip show Flask-Limiter 
Name: Flask-Limiter
Version: 3.12
Summary: Rate limiting for flask applications
Home-page: https://flask-limiter.readthedocs.org
Author: Ali-Akber Saifee
Author-email: ali@indydevs.org
License: MIT
Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
Requires: Flask, limits, ordered-set, rich
Required-by: 
(venv) ferdinandniyongira@Ferdinands-MBP FlaskAPI-ApplicationFactoryPattern-


# Editing our Many-to-Many Relationships

# Creating Insightful endpoints Capitalizing on our Relationships

Implementing Sorting Keys to make Insightful queries.

# Applying a query parameter to refine our searching


# Incorporating Query Parameters in our Endpoints
What are Query Parameters?

Query parameters are key-value pairs appended to the end of a URL after the ? symbol. They provide additional information to the server and are often used to filter, sort, or limit the results in API requests.
Structure:

A URL with query parameters looks like this:
https://example.com/items?item_name=phone
The query parameter here is item_name and the value we're assigning is phone. This could be used to search our database for items with "phone" in the name or description.
Usage in APIs:

Query parameters make it easier to customize responses from an API without changing the endpoint itself.
By adding query parameters we can send information to our server, like a search term, category filter, or sort command, without having to send a full JSON payload.

# Efficient Data retrieval with Pagination
What is Pagination?

Pagination divides large sets of data into manageable chunks or pages. This is crucial in APIs to prevent overwhelming users with too much data at once.

# Pagination Methods:

Limit and Offset: These are the most common methods for pagination.
limit: Specifies how many results to return (page size).
offset or page: Skips a certain number of results (page number).
https://api.example.com/products?limit=10&offset=20
This returns 10 products, starting from the 21st product (offset 20).
Other Pagination Techniques:

# Page and Page Size:
https://api.example.com/products?page=2&page_size=10
Similar to limit and offset but uses page and page_size.
This fetches the second page with 10 results per page.
# Why Use Pagination?

Pagination enhances performance and user experience by delivering results in smaller, more digestible portions, and reduces server load.

http://127.0.0.1:5000/books?page=1&per_page=2











http://127.0.0.1:5000/books?page=1&per_page=3

