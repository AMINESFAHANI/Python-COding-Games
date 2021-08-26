import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
hex= hex(n)
n=n*int(hex[-1],16)
n=bin(n)


print(n[-1])