class ClaimRouter:
    def __init__(self, router_id, appraiser_id, verifier_id, adjuster_id) -> None:
        self.router_id = router_id
        self.requests = []
        self.appraiser_id = []
        self.verifier_id = []
        self.ajuster_id = []
