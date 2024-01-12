#!/usr/bin/python3
"""N Queens puzzle
The N queens puzzle is the fun challenge of
placing N non-attacking queens on an
N×N chessboard.
"""
import sys

# set usage
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
elif int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
else:
    N = int(sys.argv[1])

    for i in range(1, N-1):
        solution = []
        for j in range(0, N):
            solution.append([j, i])
        print(solution)
