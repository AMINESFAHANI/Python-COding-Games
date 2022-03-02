import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
l=s.split(" ")
res=[]
for i in range(len(l)):
   if l[i]:
      x=""
      x=l[i][0].upper()+l[i][1:]
      res.append(x)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(*res)
