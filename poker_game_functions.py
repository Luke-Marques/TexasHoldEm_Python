from random     import shuffle
from itertools  import cycle
from typing     import List
from table      import Table
from cards      import Deck
from entities   import Player, NPC
from monies     import Stack, Pot
    
    
def get_dealer_entity(entities: List[Player or NPC]) -> Player or NPC:
    """Function to find a dealer entity in a list of entities."""
    
    return [entity for entity in entities if entity.is_dealer][0]


def get_dealer_entity_index(entities: List[Player or NPC]) -> int:
    """Function to find the index of a dealer entity in a list of entities."""
    
    return [idx for (entity, idx) in enumerate(entities) if entity.is_dealer][0]
    

def get_small_blind_entity_index(entities: List[Player or NPC]) -> int:
    """Function to find the index of a small blind entity in a list of entities."""
    
    return [idx for (entity, idx) in enumerate(entities) if entity.is_small_blind][0]

    