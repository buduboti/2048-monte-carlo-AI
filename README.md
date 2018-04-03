# 2048-monte-carlo-AI

Game source (logic.py, puzzle.py): yangshun/2048-python

I was modifyed the game a little bit and I have written a new module (named 'ai.py').
This module use the Monte Carlo tree search (MCTS) and it have two parameters: N, M.
N is the number of random generated ways;
M is the depth of random generated ways.

The V function computes the value of a state, the test_N is computes an average of this values and the program will choose the next step by comparing this average values.
