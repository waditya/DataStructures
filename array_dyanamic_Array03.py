#!/bin/python3

n,m = map(int, input().split())
lastAnswer = 0
seqList = [[] for _ in range(n)]
for _ in range(m):
    case,x,y = [int(temp) for temp in input().split()]
    if case == 1:
        seq = (x ^ lastAnswer) % n
        seqList[seq].append(y)
    if case == 2:
        seq = (x ^ lastAnswer) % n
        lastAnswer = seqList[seq][y % len(seqList[seq])]
        print(lastAnsw
