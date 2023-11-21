<<<<<<< HEAD
class ProfileManager:
    def __init__(self):
        pass

    def getProfile(self, uid, db):
        '''
        Function to retrieve information about the user
        Parameters:
            @uid = user id
            @db = database manager
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @uid = user id
                @email = email of user
                @fistname = firstname of user
                @lastname = lastname of user
                @phoneno = phone number of user
                @gender = gender of user
                @address = address of user
                @occupation = occupation of user
                @empStatus = employment status of user
                @empName = employer/company name of user
        '''
        try:
            user_info, status_code = db.getUser(uid)
            if status_code != 200:
                return {"error": "Error retrieving user information"}, status_code

            profile = {
                "uid": user_info[0],
                "email": user_info[2],
                "firstname": user_info[3],
                "lastname": user_info[4],
                "phoneno": user_info[8],
                "gender": user_info[9],
                "address": user_info[10],
                "occupation": user_info[11],
                "empStatus": user_info[12],
                "empName": user_info[13]
            }

            return profile, 200

        except Exception as e:
            print(f"Error in getProfile: {e}")
            return {"error": "Internal server error"}, 500

    def changeProfile(self, uid, db, changeInfo):
        '''
        Function to change information about the user
        Parameters:
            @uid = user id
            @db = database manager
            @changeInfo = dictionary containing fields to change
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @message = success message
        '''
        try:
            user_info, status_code = db.getUser(uid)
            if status_code != 200:
                return {"error": "Error retrieving user information"}, status_code

            for key, value in changeInfo.items():
                # Update the user profile one field at a time
                db.updateUser(uid, key, value)

            return {"message": "Profile updated successfully"}, 200

        except Exception as e:
            print(f"Error in changeProfile: {e}")
            return {"error": "Internal server error"}, 500
=======
class ProfileManager:
    def __init__(self):
        # Add class variables and documentation as required
        pass

    def getProfile(self, uid, db):
        '''
        Function to retrieve information about the user
        Parameters:
            @uid = user id
            @db = database manager
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @uid = user id
                @email = email of user
                @fistname = firstname of user
                @lastname = lastname of user
                @phoneno = phone number of user
                @gender = gender of user
                @address = address of user
                @occupation = occupation of user
                @empStatus = employment status of user
                @empName = employer/company name of user
        '''
        try:
            user_details, status_code = db.getUser(uid)
            if status_code != 200:
                return {"error": "Error retrieving user profile"}, status_code

            profile_data = {
                "uid": user_details[0],  # Replace with the actual attribute index
                "email": user_details[1],  # Replace with the actual attribute index
                "firstname": user_details[2],  # Replace with the actual attribute index
                "lastname": user_details[3],  # Replace with the actual attribute index
                "phoneno": user_details[7],  # Replace with the actual attribute index
                "gender": user_details[8],  # Replace with the actual attribute index
                "address": user_details[9],  # Replace with the actual attribute index
                "occupation": user_details[10],  # Replace with the actual attribute index
                "empStatus": user_details[11],  # Replace with the actual attribute index
                "empName": user_details[12]  # Replace with the actual attribute index
            }

            return profile_data, 200

        except Exception as e:
            print(f"Error in getProfile: {e}")
            return {"error": "Internal server error"}, 500

    def changeProfile(self, uid, db, changeInfo):
        '''
        Function to change information about the user
        Parameters:
            @uid = user id
            @db = database manager
            @changeInfo ## complete this
        '''
        try:
            for field, value in changeInfo.items():
                db.updateUser(uid, field, value)

            return {"message": "Profile updated successfully"}, 200

        except Exception as e:
            print(f"Error in changeProfile: {e}")
            return {"error": "Internal server error"}, 500
>>>>>>> 790e11f43caca9a90baefaf65a8ff3010efc5ca8
