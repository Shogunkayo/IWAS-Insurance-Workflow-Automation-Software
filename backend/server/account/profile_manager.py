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
