N = int(input())

# 배열 입력 받기
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# 색종이 개수 저장할 변수
white_count = 0
blue_count = 0

# 색종이 검사 함수
def check_same(x, y, n):
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:
                return False
            
    return True

# 재귀함수
def go(x, y, n):
    global white_count, blue_count
    # 기저사례
    if n == 1:
        if arr[x][y] == 0:
            white_count += 1
        else:
            blue_count += 1
        return
    
    # 만약 n안의 숫자들이 모두 같다면 return
    if check_same(x, y, n):
        if arr[x][y] == 0:
            white_count += 1
        else:
            blue_count += 1
        return
   
    half = n // 2
    go(x, y, half)
    go(x, y + half, half)
    go(x + half, y, half)
    go(x + half, y + half, half)


go(0, 0, N)

print(white_count)
print(blue_count)