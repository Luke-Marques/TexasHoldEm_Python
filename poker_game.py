from betting_round_setup import betting_round_setup
from round_setup import round_setup
from game_setup import get_blinds, get_entities
from betting import entity_go
from cl_print_statements import TITLE, GAME_SETUP, PRE_FLOP, FLOP, TURN, RIVER

class PokerGame:
    
    def __init__(self) -> None:
        # what to run when poker game is initialized
        
        print(TITLE)
        
        print(GAME_SETUP)
        entities = get_entities()
        self.small_blind, self.big_blind = get_blinds()
        
        game_over = False
        round_counter = 0
        while not game_over:
            
            self.table = round_setup(entities, round_counter)
            
            betting_round_counter = 0
            while betting_round_counter < 4:
                
                if betting_round_counter == 0:
                    print(PRE_FLOP)
                elif betting_round_counter == 1:
                    print(FLOP)
                elif betting_round_counter == 2:
                    print(TURN)
                elif betting_round_counter == 3:
                    print(RIVER)
                    
                betting_round_setup(self.table, self.small_blind, self.big_blind, betting_round_counter)
                entity_go(self.table)   
                    
                betting_round_counter += 1 
                
                
