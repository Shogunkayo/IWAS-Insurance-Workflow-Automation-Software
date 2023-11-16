from functools import wraps
import MySQLdb
from flask import jsonify
from pymongo import MongoClient

class DatabaseManager:
    def __init__(self, sql_host, sql_uname, sql_pw, sql_db, mongo_host, mongo_uname, mongo_pw):
        '''
            Database Manager class to handle database queries. Contains the
            connections to both the sql and mongo databases.
            Parameters:
                @sql_host = host address of the sql server
                @sql_uname = username for the sql server
                @sql_pw = password of @sql_uname for the sql server
                @sql_db = database name of the sql database
                @mongo_host = host address of the mongo server
                @mongo_uname = username for the mongo server
                @mongo_pw = password of @mongo_uname for the mongo server
        '''
        self.sql_host = sql_host
        self.sql_uname = sql_uname
        self.mongo_host = mongo_host
        self.mongo_uname = mongo_uname

        self.sql_db = MySQLdb.connect(
            host=sql_host,
            user=sql_uname,
            password=sql_pw,
            database=sql_db
        )

        self.mongo_db = MongoClient(
            host=mongo_host,
            username=mongo_uname,
            password=mongo_pw
        )

    def closeConnection(self):
        '''
            Function to close connections to both sql and mongo databases
        '''
        self.sql_db.close()
        self.mongo_db.close()

    @staticmethod
    def _sqlCursor(f):
        '''
            Decorator to handle error checking and cursor open/close
            Parameters:
                @f = function to wrap
        '''
        @wraps(f)
        def wrapper(self, *args, **kwargs):
            '''
                Wrapper function that creates a new cursor, executes the sql
                query and closes the cursor.
                Returns:
                    On success, returns the return value of @f
                    On error, returns a tuple of JSON object and status code
                JSON object:
                    @error = error message
            '''
            try:
                cur = self.sql_db.cursor()
                db_query = f(self, *args, cur, **kwargs)
                cur.close()
                return db_query

            except Exception as e:
                print(f"error executing mysql query: {e}")
                return jsonify({'error': 'Internal server error'}), 500

        return wrapper

    @_sqlCursor
    def getPassword(self, email, cur):
        '''
            Function to retrieve user id and hashed password of @email
            Parameters:
                @email = email id of the user
                @cur = database cursor
            Returns:
                tuple of DB_Query and status code
                DB_Query: tuple =  (user id, password)
        '''
        cur.execute(f"SELECT uid, password FROM users WHERE email='{email}'")
        return cur.fetchone(), 200

    def addUser(self):
        pass

    def removeUser(self):
        pass

    def addPolicy(self, pid, startDate, endDate, premium, policyName, policyStatus, trackingStatus, paymentInfo, policyType):
        pass

    def removePolicy(self):
        pass

    def updatePolicy(self):
        pass

    def getPolicyType(self):
        pass
