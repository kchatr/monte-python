# monte-python
A Monte Carlo Simulator created in Python. 

A Monte Carlo Simulation is a simulation which is used to understand the **risk** and **uncertainty** in forecasting models (i.e. finanace, project management, cost, etc.). The underlying principle is to use randomness to solve problems that appear to be *deteministic* (a system in which randomness does not influnece the future states of said system). 

They are used for 3 types of problems: optimization; integration; 'drawing' from a probability distribution. We are concerned with the latter in this case. We have a player who's decided to test his luck against a spinner in a casino: if its between 1-51, the House wins; if its between 52-100, the player wins. We can see quite clearly that the house has a 51% chance of winning, whilst the player has a 49% chance. This simulation allows users to control the amount of money they start off with, the amount they ebt every time, the amount of rounds they play, and the amount of scenarios simulated. 

The objective of this simulation is to show the longer the player is in the game, the more money he/she is set to lose. The simple reason for this is the fact that the House has a 2% edge (51% - 49% = 2%). 

This simulation simulates a'full round', the spinner landing on a random number every 'turn'. The more scenarios the player chooses, the more holistic and interesting the results will be. The results of every scenario will be graphed on the Matplotlib chart, every line showing a seperate scenario. The player's money can be seen at every turn on every simulation. 

On average, we see the amount of money the player loses is ~2% of the betting amount. The longer you stay in the game, the more likely you are to lose. This simulation is a great way to see how a Monte Carlo system operates and how differnt variables change the simulation. 

The simulation also shows us that: 
### The house always wins

