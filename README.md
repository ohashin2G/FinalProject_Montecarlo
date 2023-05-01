# FinalProject Monte Carlo Simulator

# Metadata

Title:        **Final Project Report**\
Class:        DS 5100 \
Date:         May 2, 2023 \
Student Name: Naomi Ohashi\
Student ID:   fju4ek \
This URL:     https://github.com/ohashin2G/FinalProject_Montecarlo/edit/main/README.md
GitHub URL:   https://github.com/ohashin2G/FinalProject_Montecarlo

# Project Description

The project will implement a simple Monte Carlo simulator using a set of related classes.
The project is designed to integrate what I have learned in this class by calling upon the following areas of knowledge:
* Basic syntax, expressions, and statements in Python 
* Python Classes with initialization methods 
* Data manipulation with Pandas 
* Literate programming with docstring s and documentation 
* Unit testing with Unittest 
* Simple plotting with Pandas 
* Program modularization and packaging 

# Synopsis
## Installing
Below is an example of how you can install and set up the Monte Carlo Simulator (MCS) package.

1. Clone this repo
```ruby
git clone https://github.com/your_username_/FinalProject_Montecarlo.git
```
2. Install MCS package
```
mcs install
```

## Importing
Import class dependencies
```ruby
import pandas as pd 
import numpy as np 
import pandas as pd 
from montecarlo import Die, Game, Analyzer
```
## Scenario 2: A 6-sided die
## Creating dice
Create a fair die and two unfair dice, all of six sides with the faces 1 through 6. One unfair die (Type 1) will weight 6 five
times more than the others (i.e. it has weight of 5 and the others a weight of 1 each). The other unfair die (Type 2) will weight 1 five times more than the others.
```ruby
die_faces = [1,2,3,4,5,6]
fair_die = Die(die_faces)
Type_1_unfair = Die(die_faces)
Type_1_unfair.change_weight(6,5)
Type_2_unfair = Die(die_faces)
Type_2_unfair.change_weight(1,5)
```

## Playing games
Play a game of 10000 rolls with 2 unfair dice of type 1, 1 unfair die of type 2, and the rest fair dice.
```ruby
S2n = 10000

G4 = Game([Type_1_unfair, Type_1_unfair, Type_2_unfair, fair_die, fair_die])
G4.play(S2n)
G4.show('NARROW')
```

## Analyzing games
For each game, use an Analyzer object to determine the relative frequency of jackpots and show your results, comparing the two relative frequencies, in a simple bar chart.
```ruby
A2 = Analyzer(G3)
A2.jackpot()
fair_jackpot = A2.jackpot()/10000

A2 = Analyzer(G4)
A2.jackpot()
unfair_jackpot = A2.jackpot()/10000

objects = [fair_jackpot, unfair_jackpot]
y_frequencies = np.arange(len(objects))
jackpot_results = [fair_jackpot, unfair_jackpot]
```


# Description
Classes:
* Die class
* Game class
* Analyzer class

### Die class
A die has N sides, or “faces”, and W weights, and can be rolled to select
a face.
* W defaults to 1.0 for each face but can be changed after the object is created.
* Note that the weights are just numbers, not a normalized probability distribution.
* The die has one behavior, which is to be rolled one or more times.
* Note that what we are calling a “die” here can be any discrete random variable associated with a stochastic process, such as
using a deck of cards or flipping a coin or speaking a language.
Our probability model for such variable is, however, very simple
– since our weights apply to only to single events, we are assuming that the events are independent.

### Game class
A game consists of rolling of one or more dice of the same kind one or
more times.
* Each game is initialized with one or more of similarly defined dice (Die objects).
* By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.
* The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
* The class keeps the results of its most recent play.

### Analyzer class
An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:
* A face counts per roll, i.e. the number of times a given face appeared in each roll. For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
* A jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. all one for a six-sided die.
* A combo count, i.e. how many combination types of faces were rolled and their counts.

# Manifest
* montecarlo.py - three classes
* montecarlo_tests.py - unit tests
* montecarlo_results.txt - test results
* montecarlo_demo.ipynb - the scenario scripts







![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)
