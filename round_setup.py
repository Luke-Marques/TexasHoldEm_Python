from itertools import cycle
from typing    import List
from cards     import Deck
from entities  import Player, NPC
from table     import Table


def assign_roles_to_entities(entities: List[Player or NPC], round_counter: int) -> None:
    """Function to assign dealer, small blind, and big blind roles to entities in round of poker game."""
    
    # create cyling list
    entities_cycle = cycle(entities)
    
    # get dealer, small blind, and big blind, Player or NPC objects from entities
    for i in range(round_counter + 1):
        dealer = next(entities_cycle)
    small_blind_entity = next(entities_cycle)
    big_blind_entity = next(entities_cycle)
    
    # set roles for entities
    dealer.is_dealer = True
    small_blind_entity.is_small_blind = True
    big_blind_entity.is_big_blind = True
    
    # deletes cycle object
    del entities_cycle
    
    
def deal_cards_to_entities(table: Table) -> None:
    """Function to deal two cards to each entity."""
    
    for i in range(2):
        for entity in table.entities:
            table.deck.deal_card(entity.cards)


def round_setup(entities: List[Player or NPC], round_counter: int) -> Table:
    """Function to assign roles and deal cards to entities at the start of a round of poker, and return a new Table instance."""
    
    print(f'''\n{'-'*50}\nROUND {round_counter+1}\n''')

    # give dealer, small blind, and big blind roles to Player or NPC entities
    assign_roles_to_entities(entities=entities, round_counter=round_counter)
    
    # create table
    table = Table(entities)
    
    # deal cards to entities
    deal_cards_to_entities(table)
    
    return table
