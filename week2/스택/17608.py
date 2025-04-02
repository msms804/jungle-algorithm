import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    stack.append(int(sys.stdin.readline()))


cnt = 1
max_h = stack[-1]

while stack:
    tmp = stack.pop()

    if tmp > max_h: # 팝 한 요소가 최대높이보다 높다면
        cnt += 1
        max_h = tmp # 최대 높이 갱신

print(cnt)