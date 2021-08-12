import math


def squares(a, b):
    c=0
    for i in range(int(math.sqrt(a)),b):

       if a<= i*i <=b:
          c+=1
       if i*i>b:
           break
    return c
print(squares(24,49))