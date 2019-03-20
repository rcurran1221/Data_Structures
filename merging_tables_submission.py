# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    global parent
    
    if table != parent[table]:
        parent[table] = getParent(parent[table])
        
    return parent[table]

def merge(destination, source):
    global ans
    global lines
    global parent
    
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False
    
    lines[realDestination] += lines[realSource]
    lines[realSource] = 0
    parent[realSource] = realDestination
    
    if lines[realDestination] > ans:
        ans = lines[realDestination]
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
    
