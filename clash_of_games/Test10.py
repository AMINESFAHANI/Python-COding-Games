import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = input()
if s.islower():
    end="z"

else:
    end="Z"

x=s
r=""
for i in range(n):
    m=ord(x)%ord(end)
    if m==0:
       r+=end
       x=s
    else:
       r+= chr(ord(x)%ord(end))
       x= chr(ord(x)+1)
print(r)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

