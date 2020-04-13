# Game of Life
## Background
>The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.


>The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine. --from Wikipedia

Sadly on 11 April 2020, at age 82, John Horton Conway died of COVID-19 at his home in New Jersey.   

After hearing this news, I tried to realize the game with python.

## Require
pygame
python

## Implementation
By the way, this is also a question on the leetcode, the introduction is below.


>Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

>>1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
>>2. Any live cell with two or three live neighbors lives on to the next generation.
>>3. Any live cell with more than three live neighbors dies, as if by over-population.
>>4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

> Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.


My implementation is a simple one. First, the program generates a matrix with random 1 and 0. Then traverse each cell of the copy of matrix, and check around the 8 surrounding cells. Finally,we could get the origin matrix updated based on the result. The visualization is based on pygame, and the updating speed is slowed to 1 frame/sec.

![Image](https://github.com/Blue-Sail/Noob/blob/master/Game%20Of%20Life/pic.png)


