from dataclasses import dataclass
from typing import List
from cards import Card
from players import Player, NPC
from monies import Pot


class Table:
    """Table object."""
    
    def __init__(
        self,
        players: List[Player or NPC]
    ):
        self.players = players
        self.pot = Pot()
        self.cards = []
        
    def show_players(self):
        print('Players at table:')
        for player in self.players:
            print(player.__str__())
    
    def show_pot(self):
        print('Amount in pot:', self.pot)
        
    def show_cards(self):
        print('Cards on table:', [card.__str__() for card in self.cards])

    