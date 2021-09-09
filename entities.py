from names  import get_full_name
from monies import Stack



class Player:
    """Poker game player object."""

    def __init__(self, name: str, starting_stack_amount: int = 100) -> None:
        self.name = name
        self.stack = Stack(starting_amount=starting_stack_amount)
        self.betting_stack = Stack(starting_amount=0)
        self.cards = []
        self.is_dealer = False
        self.is_small_blind = False
        self.is_big_blind = False
        self.has_called = False
        self.poker_hand = None
        
    def __str__(self):
        return self.name
    
    @staticmethod
    def __display_check_message() -> None:
        print('*knock knock*')
        print('Checking.')
    
    @staticmethod
    def __display_call_message(call_amount: int) -> None:
        print('Calling:', call_amount)
        
    @staticmethod
    def __display_bet_message(bet_amount: int) -> None:
        print('Betting:', bet_amount)
        
    @staticmethod
    def __display_raise_message(call_amount: int, raise_amount: int,) -> None:
        print('Calling:', call_amount)
        print('Raising:', raise_amount)
        
    @staticmethod
    def __display_fold_message() -> None:
        print('Cards discarded.')
    
    def __get_raise_amount(self, min_raise_amount: int, call_amount: int) -> int:
        print('Amount in your stack:', self.stack.amount)
        print('Amount needed to call:', call_amount)
        print('Minimum to riase:', min_raise_amount)
        while True:
            try:
                raise_amount = int(input('How much would you like to raise by? ').strip())
                if raise_amount < 0:
                    print('Please enter a positive integer.')
                elif raise_amount < min_raise_amount:
                    print(f'You must raise by at lease {min_raise_amount}.')
                elif raise_amount > self.stack.amount - call_amount:
                    print(f'You do not have enough in your stack to riase by {raise_amount}.')
                elif raise_amount == self.stack.amount - call_amount:
                    print('ALL IN!')  # PLACEHOLDER
                    return raise_amount
                else:
                    return raise_amount
            except ValueError:
                print('Please enter a valid, positive integer.')
    
    def check(self) -> None:
        self.__display_check_message()

    def call(self, call_amount: int) -> None:
        if call_amount == 0:
            self.check()
        else:
            self.__display_call_message(call_amount=call_amount)
            self.stack.pay(pay_amount=call_amount, loc_stack=self.betting_stack)
            self.stack.show_amount()
        self.has_called = True
            
    def bet(self, bet_amount: int, table) -> None:
        self.__display_bet_message(bet_amount=bet_amount)
        self.stack.pay(pay_amount=bet_amount, loc_stack=self.betting_stack)
        table.set_has_called_flags(status=False)
        self.has_called = True
        self.stack.show()

    def raise_(self, min_raise_amount: int, call_amount: int, table) -> None:
        raise_amount = self.__get_raise_amount(min_raise_amount, call_amount)
        self.__display_raise_message(call_amount, raise_amount)
        self.stack.pay(pay_amount=call_amount+raise_amount, loc_stack=self.betting_stack)
        table.current_raise = raise_amount
        table.set_has_called_flags(status=False)
        self.has_called = True
        self.stack.show_amount()
       
    def fold(self, table) -> None:
        for i in range(len(self.cards)):
            table.discarded_cards.append(self.cards.pop())
        table.folded_entities.append(self)
        self.__display_fold_message()

    def show_cards(self) -> None:
        print('Cards in hand:', [card.__str__() for card in self.cards])
        

class NPC(Player):
    """Poker game non-player character object."""
    
    def __init__(self, name: str, starting_stack: int = 100) -> None:
        self.name = name
        self.stack = starting_stack
        super().__init__(name=self.name, starting_stack_amount=self.stack)
        
    def __str__(self):
        return f'{self.name} (NPC)'
