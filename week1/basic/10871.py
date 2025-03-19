# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N, X = map(int, input().split())

# 1. 수열 입력받기
arr = map(int, input().split())

# 2. for문 X 보다 작으면 출력
for a in arr:
    if(a < X):
        print(a, end=" ")
