import sys

N, B = map(int, sys.stdin.readline().split())

matrix = []

for i in range(N):
    for j in range(1):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

## 행렬 A와 B를 곱하는 함수
def matrix_mult(A, B, N):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000

    return result

def matrix_pow(A, B, N):
    """
    행렬 A를 B제곱하는 함수 (A^B)
    -분할 정복을 이용해 빠르게 거듭제곱을 계산
    """

    # 기저사례 B == 1인 경우
    if B == 1:
        return [[A[i][j] % 1000 for j in range(N)] for i in range(N)]
    
    # 재귀 호출
    half = matrix_pow(A, B // 2, N)
    half = matrix_mult(half, half, N)

    # B가 홀수이면 한번 더 A 곱해줌
    if B % 2 == 1:
        half = matrix_mult(half, A, N)

    return half

res = matrix_pow(matrix, B, N)
for row in res:
    print(*row)
