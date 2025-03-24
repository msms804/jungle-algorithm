import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([])

for i in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        queue.append(s[1])

    elif s[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else: 
            # queue의 pop(0)은 시간초과 파이썬에서는 deque 쓰는게 더 빠름
            # 시간복잡도가 O(n)으로 느림
            print(queue.popleft()) 
    
    elif s[0] == "size":
        print(len(queue))
    
    elif s[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    
    elif s[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])

    elif s[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
