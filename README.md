# Sliding Puzzle Solver

### The main goal of this program is to 

1. Go through the paces of the A* algorithm on a  toy problem
2. Study the details of a memory bounded variant of the algorithm, IDA*

The program can solve 8 and 15 tile puzzles.  The tile problem is where you are given a matrix of numbers in a  n x n  board  with one blank tile. Given a scrambled initial order, your goal is to move the tiles over the blank space to achieve the final configuration, all numbers in the increasing order with the blank tile n space 9.

*puzzleSolver.py* takes as input an 8 or a 15 puzzle and outputs the set of moves required to solve the problem. 
 
The program runs from the command line as follows: 
 
>_python puzzleSolver.py Algorithm N INPUT-FILE-PATH OUTPUT-FILE-PATH_


>where, 
> * Algorithm: 1 = A* and 2 = Memory bounded variant(IDA*) 

> * N: 3 = 8-puzzle 4 = 15-puzzle format. 

> * INPUT-FILE-PATH = The path to the input file.
 
> * OUTPUT-FILE-PATH = The path to the output file. 
 
#### e.g. The command _python puzzleSolver.py 1 3 input1.txt test-output.txt_  runs the A* algorithm on the 8 puzzle provided in input1.txt and write the moves out in test-output.txt. 
