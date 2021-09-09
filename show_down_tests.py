from show_down import *


def is_royal_flush_test() -> bool:
    
    print('----------------------------------')
    print('testing is_royal_flush fucntion...\n')
    
    my_hand = [Card(Rank.ACE, Suit.HEART), 
           Card(Rank.KING, Suit.HEART)]

    flush_com_cards = [Card(Rank.QUEEN, Suit.HEART),
                       Card(Rank.JACK, Suit.HEART),
                       Card(Rank.TEN, Suit.HEART),
                       Card(Rank.TWO, Suit.CLUB),
                       Card(Rank.THREE, Suit.SPADE)]

    non_flush_com_cards1 = [Card(Rank.FOUR, Suit.HEART),
                            Card(Rank.JACK, Suit.HEART),
                            Card(Rank.TEN, Suit.HEART),
                            Card(Rank.TWO, Suit.CLUB),
                            Card(Rank.THREE, Suit.SPADE)]

    non_flush_com_cards2 = [Card(Rank.QUEEN, Suit.CLUB),
                            Card(Rank.JACK, Suit.HEART),
                            Card(Rank.TEN, Suit.HEART),
                            Card(Rank.TWO, Suit.CLUB),
                            Card(Rank.THREE, Suit.SPADE)]
    
    flush_com_cards2 = [Card(Rank.QUEEN, Suit.HEART),
                        Card(Rank.JACK, Suit.HEART),
                        Card(Rank.TEN, Suit.HEART),
                        Card(Rank.ACE, Suit.CLUB),
                        Card(Rank.THREE, Suit.SPADE)]

    print('test 1 - should be True')
    bool1 = is_royal_flush(my_hand, flush_com_cards)
    print(bool1, end='\n\n')
    
    print('test 2 - should be False')
    bool2 = is_royal_flush(my_hand, non_flush_com_cards1)
    print(bool2, end='\n\n')
    
    print('test 3 - should be False')
    bool3 = is_royal_flush(my_hand, non_flush_com_cards2)
    print(bool3, end='\n\n')
    
    print('test 4 - should be True')
    bool4 = is_royal_flush(my_hand, flush_com_cards2)
    print(bool4, end='\n\n')
    
    if bool1 == bool4 == True and bool2 == bool3 == False:
        result = True
    else:
        result = False
        
    print('\nfunction works:', result)
 
 
def is_straight_test() -> bool:
    
    print('----------------------------------')
    print('testing is_straight_test fucntion...\n')
    
    my_hand = [Card(Rank.TWO, Suit.HEART),
               Card(Rank.THREE, Suit.DIAMOND)]
    
    straight_com_cards1 = [
        Card(Rank.FOUR, Suit.DIAMOND),
        Card(Rank.FIVE, Suit.SPADE),
        Card(Rank.SIX, Suit.CLUB),
        Card(Rank.JACK, Suit.CLUB),
        Card(Rank.KING, Suit.HEART)
    ]
    
    straight_com_cards2 = [
        Card(Rank.FOUR, Suit.DIAMOND),
        Card(Rank.FIVE, Suit.SPADE),
        Card(Rank.SIX, Suit.CLUB),
        Card(Rank.SIX, Suit.HEART),
        Card(Rank.FIVE, Suit.CLUB)
    ]
    
    straight_com_cards3 = [
        Card(Rank.FIVE, Suit.DIAMOND),
        Card(Rank.SIX, Suit.SPADE),
        Card(Rank.SEVEN, Suit.CLUB),
        Card(Rank.EIGHT, Suit.HEART),
        Card(Rank.NINE, Suit.CLUB)
    ]
    
    non_straight_com_cards1 = [
        Card(Rank.FOUR, Suit.DIAMOND),
        Card(Rank.FIVE, Suit.SPADE),
        Card(Rank.SEVEN, Suit.CLUB),
        Card(Rank.EIGHT, Suit.HEART),
        Card(Rank.NINE, Suit.CLUB)
    ]
    
    print('test 1 - should be True')
    bool1 = is_straight(my_hand, straight_com_cards1)
    print(bool1, end='\n\n')
    
    print('test 2 - should be True')
    bool2 = is_straight(my_hand, straight_com_cards2)
    print(bool2, end='\n\n')
    
    print('test 3 - should be True')
    bool3 = is_straight(my_hand, straight_com_cards3)
    print(bool3, end='\n\n')
    
    print('test 4 - should be False')
    bool4 = is_straight(my_hand, non_straight_com_cards1)
    print(bool4, end='\n\n')
    
    if bool1 == bool2 == bool3 == True and bool4 == False:
        result = True
    else:
        result = False
    
    print('\nfunction works:', result)
    
# run tests
is_royal_flush_test()
is_straight_test()

