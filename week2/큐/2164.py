import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list(range(1, N + 1))
queue = deque(arr)

while len(queue) > 1:
    # 1. 첫번째 요소 버리기
    queue.popleft()

    # 2. 첫번째 요소 push
    n = queue.popleft()
    queue.append(n)

print(queue[0])

