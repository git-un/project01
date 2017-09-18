
This repo contains code for first assignment for the course **SI 507**.

**SI507F17_project1_cards.py** is the code to be tested.
SI507F17_project1_cards.py imports **helper_functions.py**

**SI507F17_project1_tests.py** is the Unittest module based test code. Inside SI507F17_project1_tests.py, I have created tests that check boundary conditions on code in SI507F17_project1_cards.py. In total ***3 bugs*** have been reported. The bugs have been found at: 
* Face cards in the Deck do not have string name. e.g. 1 of diamond suit is not a string name i.e Ace of Diamonds
* deal_hand method does not show index error for -53 when there are only 52 cards. At the same time, the method deal_hand of Deck class does not accept an integer value greater tha 26.
* Card constructor accepts 0 as a valid rank implying 0 of Diamonds.

**Requirements.txt** contains a list of items to be installed using pip install like so.
