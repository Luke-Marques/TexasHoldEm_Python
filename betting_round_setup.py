from typing import List
from entities import Player, NPC
from table import Table


def get_dealer_entity(entities: List[Player or NPC]) -> Player or NPC:
    """Function to find a dealer entity in a list of entities."""
    
    return [entity for entity in entities if entity.is_dealer][0]


def get_small_blind_entity(entities: List[Player or NPC]) -> Player or NPC:
    """Function to find a small blind entity in a list of entities."""
    
    return [entity for entity in entities if entity.is_small_blind][0]
    

def get_big_blind_entity(entities: List[Player or NPC]) -> Player or NPC:
    """Function to find a big blind entity in a list of entities."""

    return [entity for entity in entities if entity.is_big_blind][0]


def pay_blinds_to_pot(table: Table, small_blind: int, big_blind: int) -> None:
    """Function to make the small and big blind entities pay their blinds to the table pot."""
    
    entities = table.entities
    small_blind_entity = get_small_blind_entity(entities)
    big_blind_entity = get_big_blind_entity(entities)
    
    for entity, blind_amount, blind in [(small_blind_entity, small_blind, 'small blind'), (big_blind_entity, big_blind, 'big blind')]:
        print(f'{entity.name} pays {blind} ({blind_amount}) to pot.')
        entity.stack.pay(pay_amount=blind_amount, loc_stack=entity.betting_stack)
        table.show_pot()
        

def rotate_list(l: list, idx: int) -> list:
    """Function to rotate a list about a given index."""

    return l[idx:] + l[:idx]


def get_small_blind_entity_index(entities: List[Player or NPC]) -> int:
    """Function to find the index of a small blind entity in a list of entities."""
    
    small_blind_entity = get_small_blind_entity(entities=entities)

    return entities.index(small_blind_entity)


def get_big_blind_entity_index(entities: List[Player or NPC]) -> int:
    """Function to find the index of a big blind entity in a list of entities."""
    
    big_blind_entity = get_big_blind_entity(entities=entities)

    return entities.index(big_blind_entity)


def get_first_betting_entity_index(entities: List[Player or NPC], is_pre_flop: bool) -> int:
    """Function to determine the first betting entity in a list of entities."""
    
    if is_pre_flop:
        big_blind_entity_index = get_big_blind_entity_index(entities)
        num_entities = len(entities)
        return (big_blind_entity_index + 1) % num_entities
    else:
        small_blind_entity_index = get_small_blind_entity_index(entities)
        num_entities = len(entities)
        return (small_blind_entity_index + 1) % num_entities


def rotate_entities(table: Table, betting_round_counter: int) -> None:
    """Function to rotate list of entities in a Table instance so the first entity in the list is the first to bet."""
    
    first_entity_index = get_first_betting_entity_index(entities=table.entities, betting_round_counter=betting_round_counter)
    table.entities = rotate_list(l=table.entities, idx=first_entity_index)
    
    
def deal_community_cards(table: Table, num_cards: int) -> None:
    """Function to deal a number of cards to a Table instances' cards list attribute."""
    
    for i in range(num_cards):
        table.deck.deal_card(location=table.cards)
        
        
def betting_round_setup(table: Table, small_blind: int, big_blind: int, betting_round_counter: int) -> None:
    """Function to make entities pay blinds, deal community cards, and rotate entities list according to play order."""
    
    # make small blind and big blind entities pay blinds to table pot
    if betting_round_counter == 0:
        pay_blinds_to_pot(table=table, small_blind=small_blind, big_blind=big_blind)
    elif betting_round_counter == 1:
        deal_community_cards(table=table, num_cards=3)
    else:
        deal_community_cards(table=table, num_cards=1)
    
    # rotate entities list so first entity in list is first better
    if betting_round_counter == 0:
        is_pre_flop = True
    else:
        is_pre_flop = False
    first_entity_index = get_first_betting_entity_index(entities=table.entities, is_pre_flop=is_pre_flop)
    table.entities = rotate_list(l=table.entities, idx=first_entity_index)
    