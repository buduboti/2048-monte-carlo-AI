# 2048-monte-carlo-AI

Game source (logic.py, puzzle.py): yangshun/2048-python

I have modified the game a little bit and I wrote a new module (named 'ai.py'). This module use the Monte Carlo tree search (MCTS) and it has two parameters: N, M.<br />
N is the number of random generated ways; <br />
M is the depth of random generated ways.<br />

The V function guesses the value of a state, the test_N computes an average of this values and the program will choose the next step by comparing this average values.

I have written a test module (test.py) wich is testing the parameters N and M.
