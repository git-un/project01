## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class TestCards(unittest.TestCase):
    def test_CardType(self):
    	x= Card()
    	self.assertEqual(type(x),Card,'type')

    def test_CardSuit(self):
        x=Card()
        y=type(x.suit)
        self.assertEqual(y,str,'wd be str')

    def test_RankNum(self):
    	x=Card()
    	y=type(x.rank_num)
    	self.assertEqual(y,int,'should be int')


    def test_FaceNameIsString(self):
        x= Card(0,11)
        self.assertEqual(str(x),"Ace of Diamonds","Face card with number 1, 11, 12, 13 should have string name like Ace, Jack, Queen, King respectively")

    def test_CardRankIsNotZero(self):
        x=Card(0,0)
        self.assertNotEqual(str(x), "0 of Diamonds", "Card Constructor should not accept 0 as a possible rank level because there is no card called '0 of Diamonds'")
        #Note: Code Description says we can assume no one enters an invalid rank 'less than zero'
        #but it does not say 'less than or euqal to zero'.
        #The boundary condition of 'rank level = 0' is tested here.
    def test_Pop(self):
        d= Deck()
        self.assertRaises(TypeError,d.pop_card,2.4)
    def test_Handof26(self):
        d=Deck()
        hand=d.deal_hand(26)
        d_string=str(d)
        d_list = d_string.split('\n')
        l=len(d_list)
        self.assertEqual(l,26,"A hand should be able to be dealt with the full size of the current deck")


    def test_HandofPostive52(self):
        d=Deck()
        self.assertRaises(IndexError,d.deal_hand,52)

    def test_HandofNegative53(self):
        d=Deck()
        self.assertRaises(IndexError,d.deal_hand,-53)


    def test_Linebreaks(self):
        x=Deck()
        l=str(x)
        self.assertEqual(l.count('\n'),51,'should be 51')



if __name__ == '__main__':
    unittest.main(verbosity=2)
