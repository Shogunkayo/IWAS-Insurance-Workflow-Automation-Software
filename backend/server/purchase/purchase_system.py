class PurchaseSystem:
    def __init__(self, n_routers, max_router_load, db):
        self.n_routers = n_routers
        self.max_router_load = max_router_load
        self.routers = []
        self.docVerIds = self.getDocVerifiers(db)
        self.approverIds = self.getApprovers(db)
        self.bufferReq = []

    def getAvailablePolicies(self, db):
        '''
            Function to retrieve all the policies that are available for the
            customer to purchase
            Parameters:
                @db = database manager
            Returns:
                tuple of list of JSON objects and status code
            JSON object:
                On Error:
                    @error = error message
                On Success:
                    @pName = name of the policy
                    @pType = type of the policy
                    @pDurationMonths = duration of the policy
                    @premium = calculate premium
                    @claimProcess = description of how to claim the policy
                    @coverageDetails = description of the coverage of policy
                    @renewalTerms = description of renewal terms of policy
        '''
        ## implement this function
        pass

    def getDocVerifiers(self, db):
        '''
            Function to retrieve ids of document verifiers who are not in any
            purchase router.
            Parameters:
                @db = database manager
            Returns:
                list of document verifier ids
        '''
        ## implement this function
        pass

    def getApprovers(self, db):
        '''
            Function to retrieve ids of policy approval controllers who are
            not in any purchase router.
            Parameters:
                @db = database manager
            Returns:
                list of policy approval controller ids
        '''
        ## implement this function
        pass

    def storeFile(self, file):
        '''
            Function to store files in the storage bucket.
            Parameters:
                @file = file to store
            Returns:
                tuple of JSON object and status code
            JSON object:
                On Error:
                    @errror = error message
                On success:
                    @filepath = path of the file stored
        '''
        ## implement this function, lookup how to receive files in flask and
        ## store them in server
        pass

    def createRouter(self):
        '''
            Function to create a router and append it to @self.routers if
            the number of routers is less than @self.n_routers
        '''
        ## implement this function
        pass

    def pushToRouter(self, purchaseReq):
        ''''
            Function to consolidate user information with policy purchase
            information, store the user documents, and push the job to a
            router which has load less than @self.max_router_load
            Parameters:
                @purchaseReq: JSON object of the purchase request
            JSON Object:
                @pName = name of the policy
                @pType = type of the policy
                @premium = premium of the policy
                @purchaseDate = date of purchase of the policy
                @paymentInfo = payment information of the policy
                additional keys vary based on @pType
            @pType = Vehicle
                ## add necessary info here from the database doc
            @pType = Health
                ## add necessary info here from the database doc
        '''
        ## implement this function, use self.storeFile to store file and get
        ## back filepath
        pass

    def popFromRouter(self, routerOut):
        '''
            Function to handle cleanup of a job once it has been returned from
            a router. If the policy was approved, also writes it to the
            database
            Parameters:
                @routerOut = output from the router
            Returns:
                tuple of JSON object and status code
            JSON object:
                On Error:
                    @error = error message
                On Success:
                    @pid = policy id
                    @pStatus = status of the policy (either 'active' or
                                                     'rejected')
        '''
        ## implement this function, look at the purchase router functions for
        ## @routerOut
        pass

    def deleteRouter(self):
        '''
            Function to handle cleanup of a router. The ids associated to the
            router are freed. If the router contained pending @purchaseReq,
            they are allotted to a different router.
        '''
        ## optional
        pass
