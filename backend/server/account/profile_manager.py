## Remove all comments that start with 2 hash like this

class ProfileManager:
    def __init__(self):
        ## add class variables and documentation as required
        pass

    def getProfile(self, uid):
        '''
            Function to retrieve information about the user
            Parameters:
                @uid = user id
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
        ## complete this function
        pass

    def changeProfile(self, uid, changeInfo):
        ## either find a way to change information using a single function,
        ## or create a seperate function for each field. The change info
        ## parameter changes according to how you implement
        ## The following fields can be changes: password, email, phoneno,
        ## gender, firstname, lastname, address, occupation, employmentStatus
        ## and employerName. Focus more on address, email, password and
        ## occupation first
        '''
            Function to change information about the user
            Parameters:
                @uid = user id
                @changeInfo ## complete this
        '''
        pass
