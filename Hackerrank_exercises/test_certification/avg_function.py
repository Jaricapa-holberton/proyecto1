#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*nums):
    idx = 0
    sum = 0
    check_len = len(nums)
    if (check_len <= 1):
        return (nums[0])
    else:
        while (idx < check_len):
            sum += nums[idx]
            idx += 1
        average = sum / check_len
        return (average)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()