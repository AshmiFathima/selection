#!/bin/python3

import sys

def migratoryBirds(n, ar):
    count = [0,0,0,0,0,0]
    for t in ar:
        count[t] += 1
    return count.index(max(count))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)