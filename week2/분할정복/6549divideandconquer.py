# https://codable.tistory.com/1
import sys

def get_max_area(hist, left, right):
    if left > right:
        return 0

    # 1. 최소 높이 찾기 (O(n))
    minIdx = left
    for i in range(left, right + 1):
        if hist[i] < hist[minIdx]:
            minIdx = i

    # 2. 최소 높이를 포함하는 직사각형 넓이 계산
    maxArea = hist[minIdx] * (right - left + 1)

    # 3. 왼쪽과 오른쪽 구간 재귀 호출
    leftMax = get_max_area(hist, left, minIdx - 1)
    rightMax = get_max_area(hist, minIdx + 1, right)

    # 4. 세 가지 경우 중 최대값 반환
    return max(maxArea, leftMax, rightMax)

while True:
    # 입력 처리
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        break
    n, hist = data[0], data[1:]
    
    # 분할 정복 실행
    print(get_max_area(hist, 0, n - 1))
