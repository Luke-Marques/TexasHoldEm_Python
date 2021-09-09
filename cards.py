from enum        import Enum, auto
from dataclasses import dataclass, field
from random      import shuffle


class Suit(Enum):
    """Card suits."""

    CLUB = auto()
    DIAMOND = auto()
    HEART = auto()
    SPADE = auto()

    def __str__(self) -> str:
        if self.value == 1:
            return 'Clubs'
        elif self.value == 2:
            return 'Diamonds'
        elif self.value == 3:
            return 'Hearts'
        elif self.value == 4:
            return 'Spades'

class Rank(Enum):
    """Card ranks."""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14  # ace is high in poker

    def __str__(self) -> str:
        if self.value == 11:
            return 'Jack'
        elif self.value == 12:
            return 'Queen'
        elif self.value == 13:
            return 'King'
        elif self.value == 14:
            return 'Ace'
        else:
            return str(self.value)

@dataclass(order=True, frozen=True)
class Card:
    """Playing card object."""

    sort_index: int = field(init=False, repr=False)
    rank: Rank
    suit: Suit

    def __post_init__(self) -> None:
        object.__setattr__(self, 'sort_index', self.rank.value)

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'
    
    def __add__(self, other) -> int:
        if type(other) is int:
            return self.rank.value + other
        elif type(other) is type(self):
            return self.rank.value + other.rank.value
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'")
    
    def __sub__(self, other) -> int:
        if type(other) is int:
            return self.rank.value - other
        elif type(other) is type(self):
            return self.rank.value - other.rank.value
        else:
            raise TypeError(f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(other).__name__}'")

class Deck:
    """Deck of playing cards object."""

    def __init__(self) -> None:
        self.cards = self.__get_cards()
        self.__shuffle_cards(self.cards)

    def __get_cards(self) -> list:
        # return [Card(r, s) for (r, s) in [(r, s) for r in [r for r in Rank] for s in [s for s in Suit]]]
        ranks = [rank for rank in Rank]
        suits = [suit for suit in Suit]
        ranks_and_suits = [(rank, suit) for rank in ranks for suit in suits]
        return [Card(rank, suit) for (rank, suit) in ranks_and_suits]

    def __shuffle_cards(self, cards: list) -> None:
        shuffle(cards)

    def deal_card(self, location: list) -> None:
        location.append(self.cards.pop())

    def count_remaining_cards(self) -> int:
        return len(self.cards)

    def show_cards(self) -> None:
        print('Cards in deck:')
        for card in self.cards:
            print(card.__str__())
