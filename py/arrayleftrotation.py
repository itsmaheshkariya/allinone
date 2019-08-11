#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d, n):
    newarr = []
    for i in range(len(list(a))):
        newarr.append(a[i-(int(n)-int(d))])
    return list(newarr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
