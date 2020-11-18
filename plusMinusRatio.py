#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):    
    positives = sum(x > 0 for x in arr) / len(arr)
    negatives = sum(x < 0 for x in arr) / len(arr)
    zeroes = sum(x == 0 for x in arr) / len(arr)
    
    print(positives)
    print(negatives)
    print(zeroes)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

"""
 * Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. 
Each value should be printed on a separate line with  6 digits after the decimal. 
The function should not return a value.

Print the following  3 lines, each to  6 decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

6
-4 3 -9 0 4 1         

Sample Output
0.500000
0.333333
0.166667

"""