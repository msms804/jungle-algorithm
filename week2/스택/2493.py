# 단조감소스택으로 풀 수 있다고..
import sys
N = int(sys.stdin.readline())

tops = list(map(int, sys.stdin.readline().split()))
stack = []
ret = [0] * N
# 6 9 5 7 4
for i in range(N):
    while stack:
        if stack[-1][1] < tops[i]:
            stack.pop()
        else:
            ret[i] = stack[-1][0] + 1 # 스택의 가장 탑의 인덱스 + 1 저장(즉 레이저 닿는..)
            break # 레이저 닿는곳 찾았으므로, pop을 그만하고 다음요소 푸시해야
    stack.append((i, tops[i]))
# print(*ret)

for r in ret:
    print(r, end=" ")

