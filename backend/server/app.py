from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
import bcrypt
import jwt
import MySQLdb
import sys

# Loading in environment file
load_dotenv()

# Initializing flask app
app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initializing sql connection
try:
    sql = MySQLdb.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PASSWD'),
        database=os.getenv('SQL_DB')
    )
except Exception as e:
    print(f"Error establishing sql connection: {e}")
    sys.exit(1)

# Setting up CORS
CORS(app)


# -------------- Server Routes
@app.route('/', methods=['GET'])
def root():
    '''
        Root url, to test whether the server is running
    '''
    return jsonify("Hello There")


## Authentication Routes
'''
    Authentication Routes to handle login and signup
'''


def token_required(f):
    '''
        Wrapper to validate JWT token on protected routes
        Parameters:
            @f = Original function called
        Request Objects:
            @token = JWT token
    '''
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.is_json or not isinstance(request.json, dict):
            return jsonify({'error': 'Invalid request'}, status=400)

        # Retrieve JWT token from request
        token = request.json.get('token')
        if not token:
            return jsonify({'error': 'Missing JWT'}, status=400)

        try:
            # Attempts to validatee the JWT token. Raises an exception on decoding errors
            _ = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({'error': 'Invalid JWT'}, status=401)
        
        # If the token is valid, call the original function
        return f(*args, **kwargs)
    return decorated


@app.route('/login', methods=['POST'])
def login():
    '''
        Function to handle login
        Methods:
            POST
        Request Objects:
            @email = email of the user
            @password = password of the user
        Returns:
            @error = error message if any error is encountered
            @token = JWT token for the user
            @uid = user id of the user
    '''
    if not request.is_json or not isinstance(request.json, dict):
        return jsonify({'error': 'Invalid request'}, status=400)

    email = request.json.get('email')
    password = request.json.get('password')
    
    if email == '' or password == '' or not isinstance(email, str) or not isinstance(password, str):
        return jsonify({'error': 'Invalid email or password'}, status=400)

    try:
        # Query the database for the user id and hashed password
        cur = sql.cursor()
        cur.execute(f"SELECT uid, password FROM users WHERE email = '{email}'")
        hashed = cur.fetchone()
        cur.close()
        print(hashed)
        
        # Validate the password received
        if not bcrypt.checkpw(password.encode(), hashed[1]):
            return jsonify({'error': 'Incorrect email or password'}, status=400)
        
        # Generate the JWT with an expiration period on validating the password
        token = jwt.encode({
            'user': email,
            'expiration': str(datetime.utcnow() + timedelta(days=1))
        }, app.config['SECRET_KEY'])

        return jsonify({'token': token, 'uid': hashed[0]})

    except Exception as e:
        print(f"Error executing MySQL query: {e}")
        return jsonify({'error': 'Internal server error'}, status=500)


## User Routes
@app.route('/profile', methods=['POST'])
@token_required
def hehe():
    return "welcome to dashboard"

if __name__ == '__main__':
    app.run(debug=True)
