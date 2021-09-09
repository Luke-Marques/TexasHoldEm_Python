from enum import Enum, auto
from typing import List, Tuple
from cards import Rank, Suit, Card


class PokerHandType(Enum):
    
    HIGH_CARD = auto()
    PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_FLUSH = auto()

class PokerHand:
    
    def __init__(self, hand: List[Card], community_cards: List[Card]) -> None:
        self.cards = hand + community_cards
        self.hand_ranks: Rank or Tuple[Rank]
        self.hand_type: PokerHandType
        self.hand = self.__get_best_hand()
        
    def __is_royal_flush(self) -> List[Card] or bool:
        """Function to determine if royal flush cards are present in a set of cards, and return the royal flush cards present.
        Royal flush = A, K, Q, J, 10, all the same suit."""
        
        cards = self.cards.copy()
        
        royal_flush_ranks = [Rank.ACE, Rank.KING, Rank.QUEEN, Rank.JACK, Rank.TEN]
        
        for suit in Suit:
            royal_flush_hand = [card for card in cards if (card.suit == suit) and (card.rank in royal_flush_ranks)]
            if len(royal_flush_hand) == 5:
                self.hand_type = PokerHandType.ROYAL_FLUSH
                return royal_flush_hand
        else:
            return False
    
    def __is_straight(self) -> List[Card] or bool:
        """Function to determine if straight cards are present in a hand and the community cards.
        Straight = Five cards in a sequence. """
        
        cards = self.cards.copy()
        
        cards_sorted = sorted(cards, key=lambda x: x.rank.value)
        # remove duplicate ranks
        [cards_sorted.remove(card) for card in cards_sorted if len([x for x in cards_sorted if x.rank.value == card.rank.value]) > 1]
        
        for i in range(len(cards_sorted) - 4):
            if cards_sorted[i].rank.value == cards_sorted[i+1]-1 == cards_sorted[i+2]-2 == cards_sorted[i+3]-3 == cards_sorted[i+4]-4:
                self.hand_type = PokerHandType.STRAIGHT
                return cards_sorted[i:i+5]
        else:
            return False
                
    def __is_flush(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        card_suits = [card.suit for card in cards]
        for suit in Suit:
            if card_suits.count(suit) >= 5:
                best_flush_hand = sorted([card for card in cards if card.suit is suit], key=lambda x: x.rank.value, reverse=True)
                self.hand_type = PokerHandType.FLUSH
                return best_flush_hand
        else:
            return False
    
    def __is_straight_flush(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        if self.__is_straight(self, cards):
            straight_cards = self.__is_straight(cards)
            straight_flush_cards = self.__is_flush(straight_cards)
            if straight_flush_cards:
                self.hand_type = PokerHandType.STRAIGHT_FLUSH
                return straight_flush_cards
        else:
            return False
  
    def __is_four_of_a_kind(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        card_ranks = [card.rank for card in cards]
        for rank in Rank:
            if card_ranks.count(rank) == 4:
                four_kind_hand = [card for card in cards if card.rank == rank]
                [cards.remove(card) for card in cards if card.rank == rank]
                four_kind_hand.append(max(cards, key=lambda x: x.rank.value))
                self.hand_type = PokerHandType.FOUR_OF_A_KIND
                self.hand_ranks = rank
                return four_kind_hand
        else:
            return False
        
    def __is_full_house(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        card_ranks = [card.rank for card in cards]
        three_kind_ranks = []
        pair_ranks = []
        for rank1 in Rank:
            if card_ranks.count(rank1) >= 3:
                three_kind_ranks.append(rank1)
                for rank2 in [rank for rank in Rank if rank != rank1]:
                    if card_ranks.count(rank2) >= 2:
                        pair_ranks.append(rank2)
                        best_three_kind_rank = max(three_kind_ranks, key=lambda x: x.value)
                        best_pair_rank = max(pair_ranks, key=lambda x: x.value)
                        full_house_hand = []
                        for i in range(3):
                            full_house_hand.append([card for card in cards if card.rank.value is best_three_kind_rank][i])
                        for i in range(2):
                            full_house_hand.append([card for card in cards if card.rank.value is best_pair_rank][i])
                        self.hand_type = PokerHandType.FULL_HOUSE
                        self.ranks = rank1, rank2
                        return full_house_hand
        else:
            return False

    def __is_three_of_a_kind(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        card_ranks = [card.rank for card in cards]
        sorted_cards = sorted(cards, key=lambda x: x.rank.value, reverse=True)
        for rank in Rank:
            if card_ranks.count(rank) == 3:
                three_kind_hand = [card for card in cards if card.rank == rank]
                remaining_cards = [card for card in sorted_cards if card.rank != rank]
                three_kind_hand += remaining_cards[:2]
                self.hand_type = PokerHandType.THREE_OF_A_KIND
                self.hand_ranks = rank
                return three_kind_hand
        else:
            return False
        
    def __is_two_pair(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        card_ranks = [card.rank for card in cards]
        sorted_cards = sorted(cards, key=lambda x: x.rank.value, reverse=True)
        pair_ranks = []
        for rank1 in Rank:
            if card_ranks.count(rank1) == 2:
                pair_ranks.append(rank1)
                for rank2 in [rank for rank in card_ranks if rank != rank1]:
                    if card_ranks.count(rank2) == 2:
                        pair_ranks.append(rank2)
                        best_two_pair_ranks = sorted(pair_ranks, key=lambda x: x.value, reverse=True)[:2]
                        two_pair_hand = [card for card in cards if card.rank in best_two_pair_ranks]
                        remaining_cards = [card for card in sorted_cards if card not in two_pair_hand]
                        two_pair_hand.append(remaining_cards[0])
                        self.hand_type = PokerHandType.TWO_PAIR
                        self.hand_ranks = rank1, rank2
                        return two_pair_hand
        else:
            return False
        
    def __is_pair(self) -> List[Card] or bool:
        
        cards = self.cards.copy()
        
        card_ranks = [card.rank for card in cards]
        sorted_cards = sorted(cards, key=lambda x: x.rank.value, reverse=True)
        pair_ranks = []
        for rank in Rank:
            if card_ranks.count(rank) == 2:
                pair_ranks.append(rank)
                pair_hand = [card for card in cards if card.rank in pair_ranks]
                remaining_cards = [card for card in sorted_cards if not card in pair_hand]
                pair_hand = pair_hand + remaining_cards[:3]
                self.hand_type = PokerHandType.PAIR
                self.hand_ranks = rank
                return pair_hand
        else:
            return False
        
    def __get_high_card(self) -> List[Card]:
        
        cards = self.cards.copy()
        
        sorted_cards = sorted(cards, key=lambda x: x.rank.value, reverse=True)
        self.hand_type = PokerHandType.HIGH_CARD
        self.hand_ranks = sorted_cards[0].rank
        return sorted_cards[:5]

    def __get_best_hand(self) -> List[Card]:
        
        cards = self.cards.copy()
        
        fns = [
            str.self.__is_royal_flush, 
            str.self.__is_straight_flush, 
            str.self.__is_four_of_a_kind, 
            str.self.__is_full_house, 
            str.self.__is_flush, 
            str.self.__is_straight, 
            str.self.__is_three_of_a_kind, 
            str.self.__is_two_pair, 
            str.self.__is_pair, 
            str.self.__get_high_card
        ]
        
        cards = 'set of cards'
        
        for fn in fns:
            if poker_hand := fn(cards):
                return poker_hand
        