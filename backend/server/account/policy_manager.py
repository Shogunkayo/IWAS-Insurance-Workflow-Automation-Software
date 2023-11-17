## Remove all comments that start with 2 hash like this

class PolicyManager:
    def __init__(self):
        ## add class variables and documentation as required
        pass

    def viewPolicy(self, uid, db):
        '''
            Function to retrieve information about all policies
            owned by @uid
            Parameters:
                @uid = user id
                @db = database manager
            Returns:
                tuple of list of JSON objects and status code
            JSON object:
                On Error:
                    @error = error message
                On Success:
                    @pid = policy id
                    @startDate = start date of policy
                    @endDate = end data of policy
                    @premium = calculate premium ## ask gagan on how to do this
                    @pName = policy name
                    @pStatus = status of policy
                    @pType = type of policy
        '''
        ## look at the database manager class, see what the necessary function
        ## is, speak with mayya about the queries for this and complete the 
        ## function according to the documentation above
        pass

    def cancelPolicy(self, uid, pid, db):
        '''
            Function to cancel policy @pid owned by @uid
            Parameters:
                @uid = user id
                @pid = policy id
                @db = database manager
            Returns:
                tuple of JSON object and status code
            JSON object:
                On Error:
                    @error = error message
                On Success:
                    @pid = policy id
                    @penalty = amount deducted from refund
        '''
        ## complete this function. You will have to calculate a particular
        ## penalty amount based on the type of policy, date of purchase, 
        ## premium of the policy, etc
        pass

    def renewPolicy(self):
        ## optional, ask gagan on how to renew policy 
        pass
