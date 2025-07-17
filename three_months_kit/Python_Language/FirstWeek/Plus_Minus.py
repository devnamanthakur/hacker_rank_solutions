

import math
import os
import random
import re
import sys


"""Here i have used counters to count the number of positive,ngeative and zeros numbers are there in the 
array so then i can use them to calculate the ratios and just print them out according to the question"""
def plusMinus(arr):

   positive =0
   negative =0
   zero=0
   arr_count=len(arr)
   
   for i in range(0,arr_count,1):
    if(arr[i]>0):
      positive =positive+1
    elif(arr[i]<0):
         negative = negative +1
    else:
        zero=zero+1
   print(f"{positive / arr_count:.6f}")
   print(f"{negative / arr_count :.6f}")
   print(f"{zero/arr_count:.6f}")
   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
