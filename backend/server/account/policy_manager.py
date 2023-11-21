<<<<<<< HEAD
import datetime

class PolicyManager:
    def __init__(self, db_manager):
        # You might want to initialize some variables or connect to a database here
        self.db_manager = db_manager

    def viewPolicy(self, uid):
        '''
        Function to retrieve information about all policies
        owned by @uid
        Parameters:
            @uid = user id
        Returns:
            tuple of list of JSON objects and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @pid = policy id
                @startDate = start date of policy
                @endDate = end date of policy
                @premium = calculate premium ## ask gagan on how to do this
                @pName = policy name
                @pStatus = status of policy
                @pType = type of policy
        '''
        try:
            user_policies, status_code = self.db_manager.getUserPolicy(uid)
            if status_code != 200:
                return {"error": "Error retrieving user policies"}, status_code

            policy_info_list = []
            for policy_id in user_policies:
                policy_details, _ = self.db_manager.getPolicyDetails(policy_id)
                policy_info_list.append({
                    "pid": policy_id,
                    "startDate": policy_details["start_date"],
                    "endDate": policy_details["end_date"],
                    # Add other details as needed
                })

            return policy_info_list, 200

        except Exception as e:
            print(f"Error in viewPolicy: {e}")
            return {"error": "Internal server error"}, 500

    def cancelPolicy(self, uid, pid):
        '''
        Function to cancel policy @pid owned by @uid
        Parameters:
            @uid = user id
            @pid = policy id
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @pid = policy id
                @penalty = amount deducted from refund
        '''
        try:
            user_policies, status_code = self.db_manager.getUserPolicy(uid)
            if status_code != 200:
                return {"error": "Error retrieving user policies"}, status_code

            if pid not in user_policies:
                return {"error": "Policy not found or does not belong to the user"}, 404

            penalty = self.calculate_penalty(pid)
            self.db_manager.cancelPolicy(uid, pid)
            
            return {"pid": pid, "penalty": penalty}, 200

        except Exception as e:
            print(f"Error in cancelPolicy: {e}")
            return {"error": "Internal server error"}, 500

'''    def calculate_penalty(self, pid):
        try:
            policy_details, _ = self.db_manager.getPolicyDetails(pid)
            current_date = datetime.datetime.now().date()
            end_date = policy_details.get("end_date")

            if end_date is not None and end_date > current_date:
                days_until_expiry = (end_date - current_date).days
                # Example: Penalty calculation based on days until expiry
                penalty_percentage = 0.05  # 5% penalty for every day
                penalty = int(policy_details.get("premium", 0) * penalty_percentage * days_until_expiry)
                return penalty if penalty > 0 else 0

        except Exception as e:
            print(f"Error in calculate_penalty: {e}")

        # Default penalty if an error occurs or policy details are missing
        return 100  # Placeholder value'''


    def renewPolicy(self, uid, pid):
        '''
        Function to renew policy @pid owned by @uid
        Parameters:
            @uid = user id
            @pid = policy id
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @pid = renewed policy id
                @newEndDate = new end date of policy
        '''
        try:
            user_policies, status_code = self.db_manager.getUserPolicy(uid)
            if status_code != 200:
                return {"error": "Error retrieving user policies"}, status_code

            if pid not in user_policies:
                return {"error": "Policy not found or does not belong to the user"}, 404

            new_end_date = self.db_manager.renewPolicy(uid, pid)
            return {"pid": pid, "newEndDate": new_end_date}, 200

        except Exception as e:
            print(f"Error in renewPolicy: {e}")
            return {"error": "Internal server error"}, 500

# Example usage:
if __name__ == "__main__":
    # Assuming db_manager is an instance of your DatabaseManager
    db_manager = DatabaseManager(sql_host, sql_uname, sql_pw, sql_db, mongo_host, mongo_uname, mongo_pw)
    test = PolicyManager(db_manager)

    # Example: Initialize the PolicyManager and perform some actions
    test_policies, status_code = test.viewPolicy("user123")
    print(test_policies)

    cancel_result, status_code = test.cancelPolicy("user123", "policy456")
    print(cancel_result)

    renew_result, status_code = test.renewPolicy("user123", "policy789")
    print(renew_result)
=======
import datetime

class PolicyManager:
    def __init__(self, db_manager):
        # You might want to initialize some variables or connect to a database here
        self.db_manager = db_manager

    def viewPolicy(self, uid):
        '''
        Function to retrieve information about all policies
        owned by @uid
        Parameters:
            @uid = user id
        Returns:
            tuple of list of JSON objects and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @pid = policy id
                @startDate = start date of policy
                @endDate = end date of policy
                @premium = calculate premium ## ask gagan on how to do this
                @pName = policy name
                @pStatus = status of policy
                @pType = type of policy
        '''
        try:
            user_policies, status_code = self.db_manager.getUserPolicy(uid)
            if status_code != 200:
                return {"error": "Error retrieving user policies"}, status_code

            policy_info_list = []
            for policy_id in user_policies:
                policy_details, _ = self.db_manager.getPolicyDetails(policy_id)
                policy_info_list.append({
                    "pid": policy_id,
                    "startDate": policy_details["start_date"],
                    "endDate": policy_details["end_date"],
                    # Add other details as needed
                })

            return policy_info_list, 200

        except Exception as e:
            print(f"Error in viewPolicy: {e}")
            return {"error": "Internal server error"}, 500

    def cancelPolicy(self, uid, pid):
        '''
        Function to cancel policy @pid owned by @uid
        Parameters:
            @uid = user id
            @pid = policy id
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @pid = policy id
                @penalty = amount deducted from refund
        '''
        try:
            user_policies, status_code = self.db_manager.getUserPolicy(uid)
            if status_code != 200:
                return {"error": "Error retrieving user policies"}, status_code

            if pid not in user_policies:
                return {"error": "Policy not found or does not belong to the user"}, 404

            penalty = self.calculate_penalty(pid)
            self.db_manager.cancelPolicy(uid, pid)
            
            return {"pid": pid, "penalty": penalty}, 200

        except Exception as e:
            print(f"Error in cancelPolicy: {e}")
            return {"error": "Internal server error"}, 500

'''    def calculate_penalty(self, pid):
        try:
            policy_details, _ = self.db_manager.getPolicyDetails(pid)
            current_date = datetime.datetime.now().date()
            end_date = policy_details.get("end_date")

            if end_date is not None and end_date > current_date:
                days_until_expiry = (end_date - current_date).days
                # Example: Penalty calculation based on days until expiry
                penalty_percentage = 0.05  # 5% penalty for every day
                penalty = int(policy_details.get("premium", 0) * penalty_percentage * days_until_expiry)
                return penalty if penalty > 0 else 0

        except Exception as e:
            print(f"Error in calculate_penalty: {e}")

        # Default penalty if an error occurs or policy details are missing
        return 100  # Placeholder value'''


    def renewPolicy(self, uid, pid):
        '''
        Function to renew policy @pid owned by @uid
        Parameters:
            @uid = user id
            @pid = policy id
        Returns:
            tuple of JSON object and status code
        JSON object:
            On Error:
                @error = error message
            On Success:
                @pid = renewed policy id
                @newEndDate = new end date of policy
        '''
        try:
            user_policies, status_code = self.db_manager.getUserPolicy(uid)
            if status_code != 200:
                return {"error": "Error retrieving user policies"}, status_code

            if pid not in user_policies:
                return {"error": "Policy not found or does not belong to the user"}, 404

            new_end_date = self.db_manager.renewPolicy(uid, pid)
            return {"pid": pid, "newEndDate": new_end_date}, 200

        except Exception as e:
            print(f"Error in renewPolicy: {e}")
            return {"error": "Internal server error"}, 500

# Example usage:
if __name__ == "__main__":
    # Assuming db_manager is an instance of your DatabaseManager
    db_manager = DatabaseManager(sql_host, sql_uname, sql_pw, sql_db, mongo_host, mongo_uname, mongo_pw)
    test = PolicyManager(db_manager)

    # Example: Initialize the PolicyManager and perform some actions
    test_policies, status_code = test.viewPolicy("user123")
    print(test_policies)

    cancel_result, status_code = test.cancelPolicy("user123", "policy456")
    print(cancel_result)

    renew_result, status_code = test.renewPolicy("user123", "policy789")
    print(renew_result)
>>>>>>> 790e11f43caca9a90baefaf65a8ff3010efc5ca8
