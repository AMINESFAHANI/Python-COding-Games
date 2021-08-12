import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

inputs = input().split()
w = inputs[0]
decor = inputs[1]
outer = int(inputs[2])
for i in range(outer):
    print(decor*11)

print(decor*(((11-len(w)-2)//2)),w,decor*((11-len(w)-2)//2))

for i in range(outer):
    print(decor*11)


