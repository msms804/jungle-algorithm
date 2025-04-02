import sys
from collections import deque
### 헷갈려어

T = int(sys.stdin.readline())

for i in range(T):
    PS = sys.stdin.readline()
    stack = deque([])

    for c in PS:
        if len(stack) == 0 :
            stack.append(c)
            continue

        if stack[-1] == "(" and c == ")":
            stack.pop()
        elif stack[-1] == c:
            stack.append(c)
        elif stack[-1] == ")" and c == "(":
            stack.append(c)

    # 스택에 남아있으면
    if stack:
        print("NO")
    else:
        print("YES")

    



