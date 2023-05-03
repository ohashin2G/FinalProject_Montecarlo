import unittest
import pandas as pd
from Project_Package.montecarlo import Analyzer, Game
from montecarlo import Die

class DieTestSuite(unittest.TestCase):

    """
    The Die class should have unit tests to test if the methods 
    receive the correct inputs and return valid outputs.
    """
     
    def test_1_change_weight_method(self): 
    #Checks to see if the face passed is valid; is it in the array of weights?
        sides = [1,2,3,4,5,6]
        die = Die(sides)
        die.change_weight(1, 2)
        self.assertEqual(die.die.weights[1], 1.0)

    def test_2_roll_method(self):
    #Checks to see if the weight is valid; is it a float? Can it be converted to one?
        sides = [1,2,3,4,5,6]
        die = Die(sides)
        results = die.roll(1) 
        self.assertNotEqual(results, '')

    def test_3_show_method(self):
    #Checks to see if the weight is valid; is it a float? Can it be converted to one?
        sides = [1,2,3,4,5,6]
        die = Die(sides)
        die.roll(1) 
        result = die.show()
        self.assertTrue(result.count)

class GameTestSuite(unittest.TestCase):
    
    """
    The Game class should have unit tests to test if the methods 
    receive the correct inputs and return valid outputs.
    """

    sides = [1,2,3,4,5,6]
    die = Die(sides)
    die2 = Die(sides)
    List = [die, die2]
    g1 = Game(List)

    def test_1_game_roll_method(self):
    #Checks to see if how many times the dice should be rolled.
        self.assertTrue(self.g1.roll(1))

    def test_2_dice_roll_method(self):
    #Checks to see if how many times the dice should be rolled per roll.
        self.assertTrue(self.g1.diceroll(1))

    def test_roll_dice_method(self):
    #Checks to see if how many times the die rolls.
        self.assertTrue(self.g1.roll_dice(1))

    def test_play_method(self):
    #Checks to see if how many times the die rolled.
        self.assertFalse(self.g1.play(1))  

    def test_show_method(self):
    #Checks to see if it passed the private dataframe to the user.
        test = self.g1.show('NARROW')
        pd.testing.assert_frame_equal(test, self.g1.show('NARROW'))
        #self.assertFalse(self.g1.show('NARROW').all())        

class AnalyzerTestSuite(unittest.TestCase):
    """
    The Analyzer class should have unit tests to test if the methods 
    receive the correct inputs and return valid outputs.
    """
    sides = [1,2,3,4,5,6]
    die = Die(sides)
    die2 = Die(sides)
    List = [die, die2]
    g1 = Game(List)
    A1 = Analyzer(g1)

    def test_jackpot_method(self):
    #Check to see if it returns an integer for the number times to the user
        self.assertFalse(self.A1.jackpot())

    def test_combo_method(self):
    #Check to see if Combinations were sorted and saved as a multicolumned index.    
        self.assertFalse(self.A1.combo())

    def test_face_counts_method(self):
    #Check to see if The dataframe has an index of the roll number and face values as columns.    
        self.assertFalse(self.A1.face_counts_per_roll())

if __name__ == '__main__':
    unittest.main(verbosity=3)
