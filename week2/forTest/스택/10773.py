import sys
from collections import deque

stack = deque([])
K = int(sys.stdin.readline())

for i in range(K):
    tmp = int(sys.stdin.readline())

    if stack and tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))