from typing import List
from entities import Player, NPC
    

def get_winning_entity(entities: List[Player or NPC]) -> Player or NPC:

    # get poker hand types
    poker_hands = {}
    for entity in entities:
        poker_hands[entity] = entity.poker_hand.hand_type.value
    
    # get entity with best poker hand
    best_poker_hand_entity = max(poker_hands, key=poker_hands.get)
    best_poker_hand = poker_hands[best_poker_hand_entity]
    
    # return all entities with the best poker hand
    return [entity for entity in entities if entity.poker_hand.hand_type.value == best_poker_hand]


    
           