class InsufficientFunds(Exception):
    def __init__(self,msg):
        self.msg=msg

class InvalidInputException(Exception):
    def __init__(self,msg):
        self.msg=msg
