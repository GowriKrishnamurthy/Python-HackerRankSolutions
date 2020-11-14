#!/bin/python3
import os
import random
import re
import sys
def simpleArraySum(ar):    
    sum = 0
    for i in ar:
        sum+=i
    
    return sum
    
if __name__ == '__main__':
    print("Enter number of elements")
    ar_count = int(input())

    print("Enter the elements")
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print('Total sum is:'+str(result) + '\n')
