# DS5100 Final Project: Monte Carlo Simulator

## Metadata

Title:        **Final Project Report**\
Class:        DS 5100 \
Date:         May 2, 2023 \
Student Name: Naomi Ohashi\
Student ID:   fju4ek \
This URL:     https://github.com/ohashin2G/FinalProject_Montecarlo/edit/main/README.md \
GitHub URL:   https://github.com/ohashin2G/FinalProject_Montecarlo

## Project Description

The project will implement a simple Monte Carlo simulator using a set of related classes.
The project is designed to integrate what I have learned in this class by calling upon the following areas of knowledge:
* Basic syntax, expressions, and statements in Python 
* Python Classes with initialization methods 
* Data manipulation with Pandas 
* Literate programming with docstring s and documentation 
* Unit testing with Unittest 
* Simple plotting with Pandas 
* Program modularization and packaging 

## Synopsis
### Installing
Below is an example of how you can install and set up the Monte Carlo Simulator package.

1. Clone this repo
```ruby
git clone https://github.com/ohashin2G/FinalProject_Montecarlo.git
```
2. Importing
```ruby
cd .\FinalProject_Montecarlo\ 
```
3. Install Montecarlo package
```ruby
pip install montecarlo
```

### Import class dependencies
```ruby
import pandas as pd 
import numpy as np 
import pandas as pd 
from montecarlo import Die, Game, Analyzer
```

### Creating dice
A die has N sides, or “faces”, and W weights, and can be rolled to select a face.
```ruby
sides = [1,2,3,4,5,6]
die = Die(sides)
results = die.roll(1) 
```
 
### Playing games
Play a game of 10000 rolls with 2 unfair dice of type 1, 1 unfair die of type 2, and the rest fair dice.
```ruby
G4 = Game([Type_1_unfair, Type_1_unfair, Type_2_unfair, fair_die, fair_die])
G4.play(S2n)
G4.show('NARROW')
```

### Analyzing games
For each game, use an Analyzer object to determine the relative frequency of jackpots and show your results, comparing the two relative frequencies, in a simple bar chart.
```ruby
A2 = Analyzer(G3)
A2.jackpot()
fair_jackpot = A2.jackpot()/10000

```

## Description
Classes:
* Die class
* Game class
* Analyzer class

## Die class
A die has N sides, or “faces”, and W weights, and can be rolled to select
a face.
* W defaults to 1.0 for each face but can be changed after the object is created.
* Note that the weights are just numbers, not a normalized probability distribution.
* The die has one behavior, which is to be rolled one or more times.
* Note that what we are calling a “die” here can be any discrete random variable associated with a stochastic process, such as
using a deck of cards or flipping a coin or speaking a language.
Our probability model for such variable is, however, very simple
– since our weights apply to only to single events, we are assuming that the events are independent.

#### Methods
 * Change the weight method
    - Takes two arguments: the face value to be changed and the new weight.
    - Checks to see if the face passed is valid.  If it is valid, change the weight of the face.
    - Checks to see if the weight is valid.  If it is valid, set the weight of the face value.
    - Parameters: face_value, new_weight (strings)
    - Return: No return value
 
 * Roll method
    - Takes a parameter of how many times the die is to be rolled; defaults to 1.
    - This is essentially a random sample from the vector of faces according to the weights.
    - Returns a list of outcomes.
    - Parameters: how many times the die is to be rolled  (integer)
    - Return: a list of outcomes
 
 * Show method
    - User can see the die’s current set of faces and weights (since the latter can be changed).
    - Returns the dataframe created in the initializer
    - Parameters: None
    - Return: the die’s current set of faces and weights
     
### Attributes
    - sides
    - weights

## Game class
A game consists of rolling of one or more dice of the same kind one or
more times.
* Each game is initialized with one or more of similarly defined dice (Die objects).
* By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.
* The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
* The class keeps the results of its most recent play.

### Methods
* Play method
    - Takes a parameter to specify how many times the dice should be rolled.
    - This results in a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.
    - Parameters: number of times to play a game (integer)
    - Return: None

* Show method
    - User can the results of the most recent play.
    - Takes a parameter to return the dataframe in narrow or wide form
        - This parameter defaults to wide form.
        - This parameter should raise an exception of the user passes an invalid option.
    - The narrow form of the dataframe will have a twocolumn index with the roll number and the die number, and a column for the face rolled
    - The wide form of the dataframe will a single column index with the roll number, and each die number as a column.
    - Parameters: type (string)
    - Return: Dataframe (Narrow or Wide)

### Attributes
    -   dice 
    - num_of_dice 
    - playdice is dataframe of these three items:
        'roll_number, 
        'die_number, 
        'face_rolled

## Analyzer class
An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:
* A face counts per roll, i.e. the number of times a given face appeared in each roll. For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
* A jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. all one for a six-sided die.
* A combo count, i.e. how many combination types of faces were rolled and their counts.

### Methods
* Jackpot method
    - Computes how many times the game resulted in all faces being identical
    - Parameters: None
    - Returns an integer for the number times to the user.
      
* Combo method
    - Computes the distinct combinations of faces rolled, along with their counts.
    - Combinations should be sorted and saved as a multicolumned index.
    - Stores the results as a dataframe in a public attribute
    - Parameters: None
    - Return: None

* Face counts per roll method
    - Computes how many times a given face is rolled in each event.
    - The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).
    - Parameters: None
    - Return: None
 
### Attributes
No attributes for the Analyzer



## Manifest
* montecarlo dir
    * montecarlo.py - three classes
    * __init__.py  
* montecarlo_tests.py - unit tests
* montecarlo_results.txt - test results
* montecarlo_demo.ipynb - the scenario scripts
* README.md - README file
* setup.py - setup file









![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)
