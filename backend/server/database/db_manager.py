## Remove all comments that start with 2 hash like this

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
            Instance Attributes:
                @sql_db = connection to the sql database
                @mongo_db = connection to the mongo database
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
            Queries the @Users table
            Parameters:
                @email = email id of the user
                @cur = database cursor
            Returns:
                tuple of DB_Query and status code
                DB_Query: (uid, password)
        '''
        cur.execute(f"SELECT uid, password FROM Users WHERE email='{email}'")
        return cur.fetchone(), 200

    @_sqlCursor
    def createUser(self):
        # optional
        pass

    @_sqlCursor
    def getUser(self, uid, cur):
        '''
            Function to retrieve all user details of @uid.
            Queries the @Users table
            Parameters:
                @uid = user id
            Returns:
                tuple of DB_Query and status code
            DB_Query: (uid, email, firstname, lastname, aadhaarid, role, dob,
                    phoneno, gender, address, occupation, employment_status,
                    employment_name)
        '''
        cur.execute(f"SELECT * FROM Users WHERE uid='{uid}'")
        return cur.fetchone(), 200

    @_sqlCursor
    def getUserByRole(self, role, cur):
        '''
            Function to retrieve the @uid s belonging to @role
            Queries the @Users table
            Parameters:
                @role = role to query
            Returns:
                tuple of DB_Query and status code
            DB_Query: [@uid, ]
        '''
        cur.execute(f"SELECT * FROM Users WHERE role='{role}'")
        return cur.fetchall(), 200

    @_sqlCursor
    def updateUser(self, uid, field, value, cur):
        '''
            Function to update an attribute of @uid
            Queries the @Users table
            Parameters:
                @uid = user id
                @field = attribute of@uid to update
                @value = value to replace with
            Returns:
                tuple of DB_Query and status code
            DB_Query: (uid, field, value)
        '''
        ## to update multiple values, discuss with sathvik on how you want to
        ## implement. Either iterate through each field in 
        ## @ProfileManager.changeProfile (easier to implement, but handling 
        ## errors might become tricky), or find a way for bulk update in sql
        ## (idk how to do this)
        cur.execute(f"UPDATE Users SET '{field}'='{value}' WHERE uid = '{uid}'")
        

    @_sqlCursor
    def getPolicy(self, cur):
        '''
            Function to retrieve the details of policies that are available
            (not expired) for purchase
            Queries the @Policies_Available table
            Returns:
                tuple of DB_Qeury and status code
            DB_Query: [(policyName, policyType, policyPremium,
                        policyDurationMonths, claimProcess, coverageDetails,
                        renewalTerms, expired),]
        '''
        cur.execute(f"SELECT * FROM Policies_Available WHERE expired = FALSE")
        return cur.fetchall(), 200

    @_sqlCursor
    def storePolicy(self, uid, pid, policyDetails, cur):
        '''
            Function that stores the mapping of @uid and @pid, stores the @pid,
            and the relevant information based on the @policyType
            Queries the @UsersPolicies, @Policies, @VehiclePolicies,
            @HealthPolicies
            Parameters:
                @uid = user id
                @pid = policy id
                @policyDetails = PolicyReq dict
            Returns:
                tuple of DB_Query and status code

            PolicyReq:
                @pid:
                    @pid = policy id
                    @purchaseDate = date of purchase of policy
                    @startDate = date from which policy starts
                    @endDate = date on which policy expires
                    @premium = premium of the policy
                    @policyName = name of the policy
                    @policyStatus = status of the policy for the user
                    @trackingStatus = status of the policy in the router
                    @paymentInfo = payment information
                    @policyType = type of the policy
                @type:
                    On @policyType = 'health':
                        @pid = policy id
                        @allergies
                        @medicalCondtions
                        @smokingStatus
                        @alcoholStatus
                        @bloodGroup
                    On @policyType = 'vehicle':
                        @pid = policy id
                        @licencePlateNo
                        @driversLicenceId
                        @vehicleType
                        @yearOfManufaction
                        @vehicleCompany
                        @vehicleModel
                        @currentMileage
                        @vehicleUsage
                        @DLPdfUrl = filepath to the driver's licence document
                        @vehiclePdfUrl = filepath to vehicle photo document
                        @vehicleCertPdfUrl = filepath to the vehicle's
                            registration certificate document

            DB_Query: (uid, pid)
        '''
        ## this function is called after the purchase has been approved and 
        ## finalized. Mongodb will take care of the actual purchase part 
        pass

    @_sqlCursor
    def updatePolicy(self, pid, field, value, ptype, ptypeField, ptypeValue, cur):
        '''
            Function to change the details of @pid
            Queries:
                If @field is specified, @value has to be specified, and
                @Policies table is queried.
                If @ptypeField is specified, @pTypeValue has to be specified,
                and the respective policy type table is queried
            Parameters:
                @pid = policy id
                @field = attribute of @pid to update
                @value = value to replace @field with
                @ptype = policy type of @pid
                @ptypeField = attribute of the respective policy type table
                    to update
                @ptypeValue = value to replace @ptypeField with
            Returns:
                tuple of DB_Query and status code
            DB_Query: (@pid, @field, @value, @ptype, @ptypeField, @ptypeValue)
        '''
        if field != None and value == None:
            return jsonify({'error': 'value not specified'}), 500

        if ptypeField != None and ptypeValue == None:
            return jsonify({'error': 'ptypeValue not specified'}), 500

        if field and value:
            try:
                cur.execute(f"UPDATE Policies SET '{field}'='{value}' WHERE pid='{pid}'")

            except:
                return jsonify({'error': 'Invalid field or value'}), 500

        if ptypeField and ptypeValue:
            try:
                if ptype == 'Vehicle' or ptype == 'vehicle':
                    cur.execute(f"UPDATE Vehicle_Policies SET '{ptypeField}'='{ptypeValue}' WHERE pid='{pid}'")

                elif ptype == 'Health' or ptype == 'health':
                    cur.execute(f"UPDATE Health_Policies SET '{ptypeField}'='{ptypeValue}' WHERE pid='{pid}'")

            except:
                return jsonify({'error': 'Invalid field or input'}), 500
        
    @_sqlCursor
    def getUserPolicy(self, uid, cur):
        '''
            Function to retrieve all policies owned by @uid
            Queries the @UsersPolicies table
            Parameters:
                @uid = user id
            Returns:
                tuple of DB_Query and status code
            DB_Query: [(@pid),]
        '''
        cur.execute(f"SELECT pid FROM User_Policies WHERE uid='{uid}'")
        return cur.fetchall(), 200