import names
from monies import Stack
from custom_exceptions import StackTooSmall

# In a game of no-limit Texas hold'em, the minimum opening raise must be at least twice the big blind, 
# and the maximum raise can be all of the chips a player has in his or her stack (an "all-in" bet).

# In fixed-limit hold'em (or just "limit hold'em), a raise is always exactly twice the big blind.

class Player:
    """Poker game player object."""

    def __init__(self, name: str, starting_stack_amount: int = 100) -> None:
        self.name = name
        self.stack = Stack(starting_amount=starting_stack_amount)
        self.cards = []
        self.is_dealer = False
        self.is_small_blind = False
        self.is_big_blind = False
        
    def __str__(self):
        return self.name

    # Action methods
    
    def call(self, amount: int, location: int) -> None:
        self.stack.pay(pay_amount=amount, location=location)
            
    def raise_(self, amount: int, location: int) -> None:
        if self.stack <= amount:
            raise StackTooSmall(stack=self.stack, amount=amount)
        else:
            self.stack.pay(pay_amount=amount, location=location)
            print('Raising:', amount)
            self.stack.show_amount()
            
    def fold(self, location: list) -> None:
        for i in range(len(self.cards)):
            location.append(self.cards.pop())
        print('Cards discarded.')
        
    def check(self) -> None:
        print('Checking.')

    def show_cards(self) -> None:
        print('Cards in hand:', [card.__str__() for card in self.cards])
        

class NPC(Player):
    """Poker game non-player character object."""
    
    def __init__(self, name: str = names.get_full_name(), starting_stack: int = 100) -> None:
        super().__init__(name, starting_stack)
        
    def __str__(self):
        return f'{self.name} (NPC)'
