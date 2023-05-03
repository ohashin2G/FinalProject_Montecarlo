# Import class dependencies here
import pandas as pd
import numpy as np
import random

## The Die class
"""
A die has N sides, or “faces”, and W weights, and can be rolled to select a face.
        - W defaults to 1.0 for each face but can be changed after the object is created.
        - Note that the weights are just numbers, not a normalized probability distribution.
        - The die has one behavior, which is to be rolled one or more times.
        - Note that what we are calling a “die” here can be any discrete random variable associated 
          with a stochastic process, such as using a deck of cards or flipping a coin or speaking a language.
"""

class Die(): 

    die = []
    sides = []
    weights = []

    # Initializer 
    def __init__(self, sides ):
        self.sides = sides
        self.weights = [1.0 for i in self.sides]
        self.die = pd.DataFrame({
            'sides': self.sides,
            'weights': self.weights
        })

    # Change the weight Method     
    def change_weight(self, face_value, new_weight):
        continuefacevalue = False
        for i in self.die.sides:
          if i == face_value:
            continuefacevalue = True

        continueweight = False
        result = type(new_weight)
        
        if result == "float":
          continueweight = True
        elif result == int:
          continueweight = True
        else: continueweight = False
         
        if continuefacevalue & continueweight:
            index = self.die.sides.index[self.die.sides == face_value].to_list()[0]
            self.die.weights[index] = new_weight
        else: print("not valid")

    # Roll the die Method
    def roll(self, n_rolls):
        results = []
        for i in range(n_rolls):
            result = self.die.sides.sample(weights=self.die.weights).values[0]
            results.append(result)
        self.results = pd.Series(results) 
        return(results)
         
    # Show Method - the die’s current set of faces and weights
    def show(self):
        return(self.die)

# The Game calss
    """
    A game consists of rolling of one or more dice of the same kind one or more times.
    """

class Game():

    dice = []
    num_of_dice = 0
    playdice = pd.DataFrame({
              'roll_number': [],
              'die_number': [],
              'face_rolled': []
          })

        # Initializer
    def __init__(self, dice: list(Die)):
        self.dice = dice
        self.num_of_dice = len(dice)
            
        # When the roll happens - return an array of roll number
    def roll(self, times):  # -> list(int):
        myres = []
        count = 0
        for element in self.dice:
          count += 1
        for i in range (1, count+1):
            for j in range (1, times+1):
                myres.append(j)
        return myres

        # When the roll happens - return an array of Die that did the roll
    def diceroll(self, times):  # -> list(int):
        myres = []
        count = 0
        for element in self.dice:
          count += 1
        for i in range (1, count+1):
            for j in range (1, times+1):
                myres.append(i)
        return myres

        # When the roll happens - return an array of the results of the die rolls
    def roll_dice(self, times: int) -> list(str, float):
        results = []
        for die in self.dice:
            results.extend(die.roll(times))
        return(results)

        # Play the game.  When this is called it sets die, roll and face values. 
    def play(self, times):
          #die_number = []
          die_number = self.diceroll(times)
          #roll_number = []
          roll_number = self.roll(times)
          #face_rolled = []
          face_rolled = self.roll_dice(times)
          
          self.playdice = pd.DataFrame({
              'roll_number': roll_number,
              'die_number': die_number,
              'face_rolled': face_rolled
          }).set_index('roll_number')


        # Show the results of the game.  This can return NARROW or WIDE results. 
    def show(self,df_type):
        continueshow = False
        if df_type == "NARROW":
            continueshow = True
        elif df_type == "WIDE":
            continueshow = True
        if not continueshow:
            print("invalid")
            return 
        if df_type == "NARROW" or df_type == "WIDE":            
            #print("showing NARROW")
            NARROW = self.playdice.set_index('die_number', append = True)
            #NARROW = pd.DataFrame(dict(self.playdice)).groupby(['die_number', 'roll_number']).face_rolled.count().to_frame('face_rolled')            
            return NARROW if df_type == "NARROW" else NARROW.unstack("die_number")


    # The Analyzer class
        """
        An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object.
        """

from pandas.core.groupby import groupby
class Analyzer ():
 
        #Initializer - Takes a game object as its input parameter
    def __init__(self, game=Game) -> None:
        self.game = game
        self.die_face_type = type(self.game.dice)
        self.combo_df = None
        self.jackpot_df = None
        self.face_counts_per_roll_df = None
        self.num_of_dice = game.num_of_dice 
        #print('num game of dice = ', game.num_of_dice)     

        #Jackpot - Compute how many times a roll resulted in all faces being the same.
    def jackpot(self):
     
        occurences_df = self.game.show('NARROW') \
            .reset_index() \
            .groupby(by=['roll_number', 'face_rolled']) \
            .size() \
            .to_frame('occurences')
        
        self.jackpot_df = occurences_df[occurences_df['occurences'] == self.num_of_dice]
        return self.jackpot_df.shape[0]
        
        #Combo - Compute how many combination types of faces were rolled and their counts.
    def combo(self):
        """
        get distinct list of WIDE results with a list
        """       
        self.combo_df = self.game.show('NARROW') \
            .groupby(by=['roll_number']) \
            .agg({'face_rolled': set}) \
            .astype({'face_rolled': 'str'}) \
            .groupby('face_rolled') \
            .size() \
            .to_frame('count_row') \
            .sort_values('count_row', ascending=False)

        #Face counts per roll - Compute how many times a given face is rolled in each event
    def face_counts_per_roll(self):  
        self.face_counts_per_roll = self.game.show('NARROW') \
            .reset_index() \
            .groupby(by=['roll_number', 'face_rolled']) \
            .size().unstack('face_rolled') \
            .fillna(0)
 
