# Context 
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
  # d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

# Task 
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Input Format

# There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

# Constraints

# Output Format

# Print the largest (maximum) hourglass sum found in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19
# Explanation

 # contains the following hourglasses:

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1        0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
  # 1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
  # 0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
  # 0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum () is:

# 2 4 4
  # 2
# 1 2 4

##Code begins

#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
arr_sum = [] ## 2-D - 4 x 4 array to store the sum of 16 hour glasses
for i in range(0,4,1):
    arr_sum.append([0,0,0,0])
max = -64
temp = 0
## arr_temp = [] --- Test Array to check the values of temp variable

## Loop to store sum of hour glasses

for i in range(0,4,1):
    for j in range(0,4,1):
        arr_sum[i][j] = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
## Loop to print the maximum element in 4 x 4 array

for i in range(0,4,1):
    for j in range(0,4,1):
        temp = arr_sum[i][j]
        ##arr_temp.append(temp)
        if temp >= max :
            max = temp
            
print(max)


           
    
   
   

