from custom_exceptions import StackTooSmall, AllIn

class Stack:
    """Stack of money object, associated with Player or NPC."""
    
    def __init__(self, starting_amount: int) -> None:
        self.amount = starting_amount
        
    def show_amount(self) -> None:
        print('Amount in stack:', self.amount)
    
    def pay(self, pay_amount: int, location: int) -> None:
        if self.amount < pay_amount:
            raise StackTooSmall(pay_amount=pay_amount, stack_amount=self.amount)
        elif self.amount == pay_amount:
            raise AllIn(pay_amount=pay_amount, stack_amount=self.amount)
        else:
            self.amount -= pay_amount
            location += pay_amount
            
class Pot(Stack):
    """Pot of money object, associated with Table."""
    
    def __init__(self) -> None:
        self.starting_amount = 0
        super().__init__(starting_amount=self.starting_amount)
        
        