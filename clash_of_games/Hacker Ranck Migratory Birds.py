#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    dic={}
    for x in arr :
       if x not in dic:
           dic[x]=arr.count(x)

    c=max(dic.values())
    n=[]
    for x in arr:
        if dic[x]==c:
            n.append(x)
    return min(n)
print(migratoryBirds([1,1,1,2,2,2,2,3,4,6,0]))