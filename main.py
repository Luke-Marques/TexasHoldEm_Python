from game_setup          import get_entities, get_blinds
from round_setup         import round_setup
from betting_round_setup import betting_round_setup
from betting             import entity_go
from show_down           import get_winning_entity
from table               import Table
from entities            import Player, NPC
from monies              import Stack, Pot
from poker_hands         import PokerHand
from cl_print_statements import TITLE, GAME_SETUP, PRE_FLOP, FLOP, TURN, RIVER


def game_loop():
    
    print(TITLE)
    
    # --- GAME SETUP ---
    
    print(GAME_SETUP)
    
    # get shuffled list of Player and NPC instances
    entities = get_entities()
    
    # get small and big blinds
    small_blind, big_blind = get_blinds()
    
    # --- ROUND LOOP ---
    
    game_over = False
    round_counter = 0
    while not game_over:  
        
        # --- ROUND SETUP ---
        
        table = round_setup(entities=entities, round_counter=round_counter)
        
        # --- BETTING ROUND LOOP ---
        
        betting_round_counter = 0  # (0, 1, 2, 3)
        while betting_round_counter < 4:
            
            if betting_round_counter == 0:
                print(PRE_FLOP)
            elif betting_round_counter == 1:
                print(FLOP)
            elif betting_round_counter == 2:
                print(TURN)
            elif betting_round_counter == 3:
                print(RIVER)
            
            betting_round_setup(table=table, small_blind=small_blind, big_blind=big_blind, betting_round_counter=betting_round_counter)
            entity_go(table=table)   
                
            betting_round_counter += 1    
            
        # --- SHOW DOWN ---
        
        for entity in table.entities:
            entity.poker_hand = PokerHand(hand=entity.cards, community_cards=table.cards)
        
        table.show_cards()
        for entity in table.entities:
            print(f'{entity.name.upper}:')
            entity.show_cards()
        winners = get_winning_entity(table.entities)
        if winners == 1:
            # announce winner
            print('Winner:', winners[0])
            # pay winner entire pot
            table.pot.pay(pay_amount=table.pot.amount, loc_stack=winners[0].stack.amount)
        elif winners > 1:
            pay_amount = table.pot.amount / len(winners)
            print('Winners:', end=' ')
            for winner in winners:
                # announce winners
                print(winner.name, end=' ')
                # pay winners proportion of pot
                table.pot.pay(pay_amount=pay_amount, loc_stack=winner.stack.amount)
            print('\n')
                
        game_over = True
                
        
game_loop()
