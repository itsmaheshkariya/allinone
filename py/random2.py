#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()
    #print(nm)
    n = int(nm[0])
    #print(n)
    m = int(nm[1])
    #print(m)
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    length = int(len(arr))
    for j in range(length):
        for i in range(length-1):
            if int(arr[i][1]) > int(arr[i+1][1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

            


    for k in range(n):
        for l in range(m):
            print(arr[k][l],end=" ")
        print()
    
    k = int(input())
