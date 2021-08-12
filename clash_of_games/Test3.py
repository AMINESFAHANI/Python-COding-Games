import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
arr=[]
for i in input().split():
    n = int(i)
    arr.append(n)
arr=sorted(arr)
odd=0
even=0
mid=arr[len(arr)//2]**2
for x in arr:
    if x%2==0:
        even+=x
    else:
        odd+=x
r=even*odd+mid


print(f"{even} * {odd} + {mid} = {r}")