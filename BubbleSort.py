#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    sort = False
    temp = 0 
    while not sort:
        sort = True
        for i in range(len(a) - 1):
        
    # compare two adjacent elements
    # change > to < to sort in descending order
         if a[i] > a[i + 1]:
        # swapping elements if elements
        # are not in the intended order
           a[i], a[i+1] = a[i+1], a[i]
           temp += 1
           sort = False
            
    print("Array is sorted in", temp, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
    return a
                      
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
