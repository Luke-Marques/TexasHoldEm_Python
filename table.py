from dataclasses import dataclass
from typing      import List
from cards       import Deck
from entities    import Player, NPC
from monies      import Pot


class Table:
    """Table object."""
    
    def __init__(self, entities: List[Player or NPC]):
        self.entities = entities
        self.pot = Pot()
        self.deck = Deck()
        self.cards = []
        self.discarded_cards = []
        self.current_raise = 0
        self.folded_entities = []
        
    def show_entities(self):
        print('Entities at table:')
        for entity in self.entities:
            print(entity.__str__())
    
    def show_pot(self):
        betting_stacks_total = sum([e.betting_stack.amount for e in self.entities])
        print('Amount in pot:', self.pot.amount + betting_stacks_total)
        
    def show_cards(self):
        print('Cards on table:', [card.__str__() for card in self.cards])
        
    def set_has_called_flags(self, status: bool) -> None:
        for entity in self.entities:
            entity.has_called = status
            
    def move_betting_stacks_to_pot(self) -> None:
        for entity in self.entities:
            entity.betting_stack.pay(
                pay_amount=entity.betting_stack.amount,
                loc_stack=self.pot
            )
    
    def remove_folded_entities(self) -> None:
        for entity in self.folded_entities:
            self.entities.remove(entity)
