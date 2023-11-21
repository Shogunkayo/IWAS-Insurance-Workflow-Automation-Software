class PurchaseRouter:
    def __init__(self, rid, docVerIds, approverIds):
        self.rid = rid
        self.docVerIds = docVerIds
        self.docVerPtr = 0
        self.approverIds = approverIds
        self.approverPtr = 0
        self.purchaseReq = []

    def sendToDocVer(self, purchaseReq):
        pass

    def sendToAprrover(self, purchaseReq):
        pass

    def sendToCustomer(self, purchaseReq):
        pass
