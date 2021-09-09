from random   import shuffle
from names    import get_first_name
from typing   import Tuple
from entities import Player, NPC


def get_num_players() -> int:
    """Function to get the number of players from user input."""
    
    while True:
        try:
            num_players = int(input('How many players are playing? '))
            if num_players <= 0:
                print('Number of players cannot be negative or zero. Please enter a positive integer.')
            else:
                return num_players
        except ValueError:
            print('Please enter a valid, positive integer.')


def get_player_name(player_num: int) -> str:
    """Function to get the name of a player from user input."""
    
    while True:
        player_name = input(f"Please enter Player {player_num}'s name: ").strip()
        if not str.strip(player_name):  # if player_name is empty or only contains whitespace
            print('Player name must contain at least one non-whitespace character.')
        else:
            return player_name
        

def get_stack_amount(player_name: str) -> int:
    """Function to get the initial stack amount of a player from user input."""
    
    while True:
        try:
            stack_amount = int(input(f"Please enter {player_name}'s initial stack amount: "))
            if stack_amount <= 0:
                print('Stack amount cannot be negative or zero. Please enter a positive integer.')
            else:
                return stack_amount
        except ValueError:
            print('Please enter a valid integer.')
            

def get_player_names_and_stack_amounts(num_players: int) -> dict:
    """Function to get the name and initial stack amount for each player."""
    
    player_names_and_stacks = {}  # player_name (key): stack_amount (value)
    
    for i in range(num_players):
        player_num = i + 1
        player_name = get_player_name(player_num=player_num)
        stack_amount = get_stack_amount(player_name)
        player_names_and_stacks[player_name] = stack_amount
    
    return player_names_and_stacks


def get_players() -> list:
    """Function to create Player instances from names and stack amounts."""
    
    # get number of player entities
    num_players = get_num_players()
    
    # get names and initial stack amounts for each player entity
    player_names_and_stacks = get_player_names_and_stack_amounts(num_players)
        
    # create Player instances for each player
    players = []
    for player_name, stack_amount in player_names_and_stacks.items():
        players.append(Player(name=player_name, starting_stack_amount=stack_amount))
    
    return players


def get_num_npcs() -> int:
    """Function to get number of NPCs from user input."""
    
    while True:
        try:
            num_npcs = int(input('How many NPCs do you want to play against? '))
            if num_npcs <= 0:
                print('Number of NPCs cannot be negative or zero. Please enter a positive integer.')
            else:
                return num_npcs
        except ValueError:
            print('Please enter a valid, positive integer.')


def get_npcs() -> list:
    """Function to create NPC instances."""
    
    # get number of NPC entities
    num_npcs = get_num_npcs()
    
    # create NPC instances for each NPC
    npcs = []
    for i in range(num_npcs):
        npcs.append(NPC(get_first_name()))
        
    return npcs


def get_entities() -> list:
    """Function to create shuffled list of Player and NPC instances."""
    
    # get lists of Player and NPC instances
    players = get_players()
    npcs = get_npcs()
    
    # combine lists to entities list containing Player and NPC instances
    entities = players + npcs
    shuffle(entities)
    
    return entities


def get_small_blind() -> int:
    """Function to get small blind amount from user input."""
    
    while True:
        try:
            small_blind = int(input('Please enter the small blind amount: '))
            if small_blind <= 0:
                print('Small blind amount cannot be negative or zero. Please enter a positive integer.')
            else:
                return small_blind
        except ValueError:
            print('Please enter a valid, positive integer.')


def get_big_blind(small_blind: int) -> int:
    """Function to get big blind amount from user input."""
    
    # In a game of no-limit Texas hold'em, the minimum opening raise must be at least twice the big blind, 
    # and the maximum raise can be all of the chips a player has in his or her stack (an "all-in" bet).

    # In fixed-limit hold'em (or just "limit hold'em), a raise is always exactly twice the big blind.

    return 2 * small_blind


def get_blinds() -> Tuple[int]:
    """Function to get small blind and big blind amount."""
    
    small_blind = get_small_blind()
    big_blind = get_big_blind(small_blind)
    
    blinds = (small_blind, big_blind)
    
    return blinds
