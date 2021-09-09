from itertools import cycle
from entities import Player, NPC
from table import Table


def display_action_command_help() -> None:
    """Function to print a help message displaying possible action selection commands."""
    
    HELP_MESSAGE = '''
--------------------- POSSIBLE ACTION COMMANDS ---------------------
                                        
check -------------- : do not add any money to the pot              
call --------------- : match the current highest bet                
raise -------------- : add at least twice the current bet to the pot
fold --------------- : discard cards and exit play until next deal
view hand ---------- : display the cards in your hand
view community cards : display cards in play on the table

--------------------------------------------------------------------
'''
    
    print(HELP_MESSAGE)
        
        
def get_action_command(table: Table) -> int:
    """Function to get desired action from user input."""
    
    valid_commands = ['check', 'call', 'raise', 'fold', 'view hand', 'view community cards']
    
    while True:
        
        command = input('What would you like to do? ').lower().strip()
        
        if (command == 'view community cards') and (len(table.cards) == 0):
            print('No community cards. Please enter a different action.')
            print('Enter "help" for a list of valid commands.')
        elif command == 'help':
            display_action_command_help()
        elif command in valid_commands:
            break
        else:
            print('Action unknown.')
            print('Enter "help" for a list of valid commands.')
            
    return command
            
            
def perform_action(entity: Player or NPC, table: Table, action: str, call_amount: int, min_raise_amount: int) -> bool:
    """Function to enact action by calling correct Player member method."""
    
    if action in ['call', 'check']:
        entity.call(call_amount=call_amount)
        return True
    elif action == 'raise':
        entity.raise_(min_raise_amount=min_raise_amount, call_amount=call_amount, table=table)
        return True
    elif action == 'fold':
        entity.fold(table)
        return True
    elif action == 'view hand':
        entity.show_cards()
        return False
    elif action == 'view community cards':
        table.show_cards()
        return False
        
        
def all_entities_called(table: Table) -> bool:
    """Function to determine if all entities at table have checked/called."""

    if all([entity.has_called for entity in table.entities]):
        # add betting stacks to pot
        for entity in table.entities:
            entity.betting_stack.pay(pay_amount=entity.betting_stack.amount, loc_stack=table.pot)
        return True
    else: return False


def entity_go(table: Table) -> bool:
    """Function to get and perform an action for an entity, and check if all entities at the table have called/checked."""
    
    # continuously loop over each entity
    all_called = False
    while not all_called:
        
        for entity in table.entities:
        
            print(f"\n{'-'*50}\n{entity.name.upper()}'S GO:\n")
                            
            # get amount needed to call
            call_amount = max([e.betting_stack.amount for e in table.entities]) - entity.betting_stack.amount
            
            # get minimum amount needed to raise
            if table.current_raise != 0:
                min_raise_amount = table.current_raise
            else:
                min_raise_amount = max([entity.betting_stack.amount for entity in table.entities])
            
            bet_action_completed = False
            while not bet_action_completed:
                if type(entity) is Player:
                    action_command = get_action_command(table=table)
                    bet_action_completed = \
                        perform_action(entity=entity, table=table, action=action_command, call_amount=call_amount, min_raise_amount=min_raise_amount)
                elif type(entity) is NPC:
                    action_command = 'call'
                    bet_action_completed = \
                        perform_action(entity=entity, table=table, action=action_command, call_amount=call_amount, min_raise_amount=min_raise_amount)
                        
            # remove any folded players from table
            if table.folded_entities:
                table.remove_folded_entities()
            
            # check if all players have checked/called
            all_called = all_entities_called(table=table)
            
            if all_called:
                break
    
    table.set_has_called_flags(status=False)
    table.move_betting_stacks_to_pot()
