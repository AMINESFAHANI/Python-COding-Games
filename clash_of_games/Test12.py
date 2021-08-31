import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

length = int(input())
map = input()
status="Small"
# Dead, Small, Tall or Overpowered"
for i in range(length):
    x=map[i]
    if x=="M" and status=="Small":
        status="Tall"
    elif x=="F" and (status=="Small" or status=="Tall"):
        status="Overpowered"





print("answer")