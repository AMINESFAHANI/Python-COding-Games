import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = [[]] * n
for i in range(n):
     if i % 2 == 0:
         a = "*"
         b = " "
     else:
         a = " "
         b = "*"
     for j in range(n):
         if j % 2 == 0:
             print(a,end="")
         else:
             print(b,end="")
     print()

            # Write an answer using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

