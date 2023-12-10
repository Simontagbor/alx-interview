# 0x0A. Prime Game

`Algorithm` `Python`

I worked on a an algorithm that determines the winner of a prime game. The game is played by two players, Maria and Ben.

The game starts with a set of consecutive integers starting from 1 up to and including n. The players take turns, Maria always going first, and the goal is to be the last one to say a prime number.

## Tasks

### 0. Prime Game

[0-prime_game.py](./0-prime_game.py): Python function that determines the winner of the prime game.

* Prototype: `def isWinner(x, nums)`
  * `x` is the number of rounds
  * `nums` is an array of `n` - the set of consecutive integers starting from `1` up to and including `n`
  * Returns the name of the player that won the most rounds
  * If the winner cannot be determined, return `None`
  * Maria always goes first
  * You can assume `n` and `x` will not be larger than 10000
  * You cannot import any packages in this task
  * Example:
    * `x` = `3`, `nums` = `[4, 5, 1]`
    * First round: `4` and `5` are removed leaving `[1]`
    * Second round: `1` is removed, leaving `[]`
    * Third round: `Maria` cannot make a move so `Ben` wins
    * Function should return `Ben`

