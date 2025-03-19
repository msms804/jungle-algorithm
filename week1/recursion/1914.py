N = int(input())

def move(n, x, y):
    # 1. 그룹을 1 -> 2로 이동
    if n > 1:
        move(n - 1, x, 6 - x - y)

    # 2. 맨 밑 기둥을 목적지로 이동
    print(x, y)

    # 3. 그룹을 2 -> 3으로 이동
    if n > 1:
        move(n - 1, 6 - x - y, y)

print(2**N - 1)

if N <= 20:
    move(N, 1, 3)

    
