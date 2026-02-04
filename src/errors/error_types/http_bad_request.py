class HttpBadRequestError(Exception):
    def __init__(self, message : str) -> None:
        super().__init__(message)
        self.status_code = 400
        self.message = message
        self.error_type = "HTTP_BAD_REQUEST"
        

