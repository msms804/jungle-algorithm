from collections import deque

N = int(input())


for i in range(N):
    stack = deque()
    ps = input() 

    for j in ps:
        if not stack: # stack 이 비었으면 푸시
            stack.append(j)
            continue

        if stack[-1] == "(" and j == ")":
            stack.pop()
        else:
            stack.append(j)

    if stack:
        print("NO")
    else:
        print("YES")