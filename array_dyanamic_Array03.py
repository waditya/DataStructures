#!/bin/python3

import sys

## Initiate varaibles

lastAnswer = 0
arr = []

#n = int(input().strip())

arr_first_line = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#print(arr_first_line) -- to print the first line [N, Q]

n = int(arr_first_line[0])
no_of_queries = int(arr_first_line[1])

print(no_of_queries)

## Create an array to hold the input queries
arr_query = []

##print(n)  ##--- Debug the value of n - number of empty sequences

for ctr in range(0,no_of_queries,1):
    arr_query_temp = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr_query.append(arr_query_temp)
    
    
##print(arr_query) ## --- Debug the value of query sequences given in input

## Create n sequnces in an array

for ctr in range(0,no_of_queries,1):
    arr.append([])

print(arr)    ## --- Debug array
len(arr)   ## --- Debug length of arr

## Function Library Definition starts

def getQueryType(arr_query_list):
    flag = -1
    if(arr_query_list[0]) == 1:
        flag = 1
    else :
        flag = 2
    return flag

## Test the code output of getQueryType function

# print(getQueryType(arr_query[0]))
# print(getQueryType(arr_query[1]))
# print(getQueryType(arr_query[2]))
# print(getQueryType(arr_query[3]))
# print(getQueryType(arr_query[4]))

def createList(arr, query_list, type, f_lastAnswer, n):
    y = query_list[2]
    x = query_list[1]
    
    
     
    if f_lastAnswer > 0:
        dup_lastAnswer = 1
    else :
        dup_lastAnswer = 0
    
    ##Rationalize inputs and parameters to binary

    if type == 1 :
        ## print(int(x ^ dup_lastAnswer) % n)
        arr[int(int(x ^ dup_lastAnswer) % n)].append(y)
        return(arr)
    else :
        size_seq = len(arr[(x ^ dup_lastAnswer) % n])
        print(size_seq)
        f_lastAnswer = arr[(x ^ dup_lastAnswer) % n][y % size_seq]
        print(f_lastAnswer)
        return(f_lastAnswer)
    
## Function Library Ends

for i in range(0, no_of_queries,1):
    if(getQueryType(arr_query[i])) == 1:
        arr = createList(arr, arr_query[i], 1, lastAnswer, n)
    else:
        lastAnswer = createList(arr, arr_query[i], 2, lastAnswer,n)
        print(lastAnswer)
        
        
#print(arr)        
    
    

