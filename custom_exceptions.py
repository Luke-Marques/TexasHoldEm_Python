class Error(Exception):
    """Base class for custom exceptions."""
    pass

class StackTooSmall(Error):
    """Raised when a Stack object's amount attribute is too small to perform action (e.g. calling).
    
    Attributes:
        pay_amount -- amount of money to remove from Stack object's amount attribute
        stack_amount -- Stack object's amount attribute
        message -- explanation of the error
    """
    
    STANDARD_MESSAGE = 'Stack is too small to perform action.'

    def __init__(self, pay_amount: int, stack_amount: int, message: str = STANDARD_MESSAGE) -> None:
        self.pay_amount = pay_amount
        self.stack_amount = stack_amount
        self.message = message
        super().__init__(self.message)
        
    def __string__(self) -> str:
        return f'Amount in stack ({self.stack_amount}) is less than the action amount ({self.pay_amount}).'
    
    
class AllIn(Error):
    """Raised when a Stack object's amount attribute is the same size as the pay amount involved in an action (e.g. raising).
    
    Attributes:
        pay_amount -- amount of money to remove from Stack object's amount attribute
        stack_amount -- Stack object's amount attribute
        message -- explanation of the error
    """
    
    STANDARD_MESSAGE = 'Performing action would result in Stack.amount attribute being zero.'

    def __init__(self, pay_amount: int, stack_amount: int, message: str = STANDARD_MESSAGE) -> None:
        self.pay_amount = pay_amount
        self.stack_amount = stack_amount
        self.message = message
        super().__init__(self.message)
        
    def __string__(self) -> str:
        return f'Amount in stack ({self.stack_amount}) is equal to the action amount ({self.pay_amount}). This means requires an All-In action.'
    
    
    
    