import sys
# 재귀함수에서는 함수 종료할때 return 꼭 해야
N = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white_count = 0
blue_count = 0

def check_same(x, y, n): 
    # 만약 모든 수가 같으면 끝
    tmp = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tmp != matrix[i][j]:
                return False            
    return True

def divide_and_conquer(x, y, n):
    global blue_count, white_count
    # 기저사례
    if n == 1:
        if matrix[x][y] == 0:
            white_count += 1
        else:
            blue_count += 1
        return # 리턴 해야 재귀 멈춤
    
    if check_same(x, y, n):
        if matrix[x][y] == 0:
            white_count += 1
        else:
            blue_count += 1
        return # 리턴 해야 재귀 멈춤

    half = n // 2
    # 1분면
    divide_and_conquer(x, y, half)
    # 2분면
    divide_and_conquer(x, y + half, half)
    # 3분면
    divide_and_conquer(x + half, y, half)
    # 4분면
    divide_and_conquer(x + half, y + half, half)


divide_and_conquer(0, 0, N)

print(white_count)
print(blue_count)