from collections import deque
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수


apples = []
directions = []
for _ in range(K): # 튜플로 받아야
    i, j = map(int, input().split())
    apples.append((i, j))

L = int(input()) # 방향 변환 횟수

for _ in range(L):
    X, C = input().split()
    # X초 후에 방향 회전
    # 왼쪽 C가 L(왼쪽으로 90도 회전)
    # 오른쪽 C 가 D(오른쪽으로 90도 회전)
    directions.append((int(X), C))



dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위 , 오른쪽, 아래, 왼쪽
snake = deque([(0, 0)]) # 뱀의 시작 위치
ret = 0

# 뱀 이동시키기
# dir = dyx[1] # 일단 오른쪽 방향으로 초기화
dir_idx = 1 # 처음방향
for d in directions:
    for i in range(d[0]): # ~초 동안 이동
        # 새로운 머리 위치 계산
        head_y, head_x = snake[0]
        new_y = dyx[dir_idx][0] + head_y
        new_x = dyx[dir_idx][1] + head_x

        # 몸통에 부딪히는 경우
        if (new_y, new_x) in snake:
            print(ret + 1)
            exit()

        # 벽에 부딪히는 경우(추후 수정)
        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
            print(ret + 1)
            exit() 
        
        # 머리를 새로운 위치로 이동
        snake.appendleft((new_y, new_x))
        ret += 1

        # 만약 사과 먹는 경우
        if (new_y, new_x) in apples:
            apples.remove((new_y, new_x))
        else:
            snake.pop()


    # 방향 바꿔야
    if d[1] == "D": # 오른쪽으로 90도 회전해야
        dir_idx = (dir_idx + 1) % 4
    elif d[1] == "L": # 왼쪽으로 90도 회전해야
        dir_idx = (dir_idx - 1) % 4

    
        


