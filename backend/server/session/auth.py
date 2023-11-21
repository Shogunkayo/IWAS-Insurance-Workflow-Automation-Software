from datetime import datetime, timedelta
import bcrypt
import jwt
from functools import wraps
from flask import jsonify, request

class SessionManager:
    def __init__(self, secret_key):
        '''
            Session Manager class to handle user authentication and registration.
            Parameters:
                @secret_key = secret key for the JWT token
        '''
        self._secret_key = secret_key

    def validateJWT(self, f):
        '''
            Decorator to validate JWT token on protected routes. Requires the
            JWT token to be in the request.
            Parameters:
                @f = function to wrap
            Returns:
                tuple of JSON object and status code on error
            JSON object:
                @error = error message
        '''
        @wraps(f)
        def wrapper(*args, **kwargs):
            '''
                Wrapper function that validates the JWT token
                Returns:
                    On success, returns the return value of @f
                    On error, returns a tuple of JSON object and status code
                JSON object:
                    @error = error message
            '''
            # Retrieve JWT token from request
            try:
                token = request.get_json()['token']
            except Exception as e:
                print("ERROR: ", e)
                return jsonify({'error': 'Missing JWT'}), 400

            try:
                # Attempts to validatee the JWT token. Raises an exception on decoding errors
                _ = jwt.decode(token, self._secret_key, algorithms=['HS256'])
            except:
                return jsonify({'error': 'Invalid JWT'}), 401

            # If the token is valid, call the original function
            return f(*args, **kwargs)
        return wrapper

    def login(self, email, password, db):
        '''
            Function to handle login
            Parameters:
                @email = email of the user
                @password = password of the user
                @db = database manager object
            Returns:
                tuple of JSON object and status code
            JSON object:
                On Error:
                    @error = error message
                On Success:
                    @token = JWT token for the user
                    @uid = user id of the user
        '''
        if (db_query := db.getPassword(email))[1] == 200:
            hashed = db_query[0]
            # Validate the password received
            if not bcrypt.checkpw(password.encode(), hashed[1]):
                return jsonify({'error': 'Incorrect email or password'}), 400

            # Generate the JWT with an expiration period on validating the password
            token = jwt.encode({
                'user': email,
                'expiration': str(datetime.utcnow() + timedelta(days=1))
            }, self._secret_key)

            return jsonify({'token': token, 'uid': hashed[0]})

        return db_query

    def signup(self):
        pass

    def writeLog(self):
        pass
