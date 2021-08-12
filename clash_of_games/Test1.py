#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    a=0
    b=0
    for i in range (0,len(arr)):
        a+=arr[i][i]
        b+=arr[i][len(arr)-i-1]
    return (abs(a-b))

arr=[[10,2,3],[4,5,6],[7,8,9]]
print(diagonalDifference(arr))
