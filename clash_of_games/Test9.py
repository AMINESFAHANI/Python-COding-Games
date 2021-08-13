# Input
# # ### # ### #
# # # # # # # #
# # ### # ### #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
line = []

for i in range(3):
    line.append(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

binary = line[0].split()

digits = [1 if len(i) == 1 else 0 for i in binary]

number = int("".join(str(i) for i in digits), 2)

print(number)