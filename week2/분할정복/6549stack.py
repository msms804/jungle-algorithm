import sys

def get_max_area(hist):
    stack = []
    max_area = 0 # 최대 넓이
    n = len(hist)

    for i in range(0, n):
        # 현재 높이가 스택의 top보다 작다면 pop하며 최대 넓이 계산
        while stack and stack[-1][1] > hist[i] : # 스택에 들어있는것 보다 작은게 들어온다면 넓이 계산
            height = stack.pop()[1]
            width = i if not stack else (i - stack[-1][0] -1)
            max_area = max(max_area, height * width)

        stack.append((i, hist[i]))

    while stack:
        height = stack.pop()[1]
        width = n if not stack else (n - stack[-1][0] -1) # n은 막대 개수
        max_area = max(max_area, width * height)
    
    return max_area

while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        break
    n, hist = data[0], data[1:]

    print(get_max_area(hist))