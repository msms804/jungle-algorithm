import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque([])
ret = 1 # 보이는 막대기 개수(맨앞은 무조건 보이므로 1로 초기화)

for i in range(N):
    h = int(sys.stdin.readline())
    stack.append(h)

max_h = stack[-1]

while stack:
    # 1. 스택의 top과 팝한 요소 비교
    tmp = stack.pop()
    if tmp > max_h:
        # 2. 만약 팝한게 더 크다면 max_h 갱신
        max_h = tmp
        ret += 1

print(ret)

