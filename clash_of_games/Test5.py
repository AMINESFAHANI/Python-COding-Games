import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
r=[["." for i in range(5)]for j in range(5)]

n=bin(n)[2:]
i=0
for x in reversed(n):
    if x=="1":
        r[4-(i//5)][4-(i%5)]=x
    i+=1
for i in range(5):
    print(r[i])
