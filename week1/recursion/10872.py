# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 시간복잡도 구해볼까?
# for문과 비교햇을때 어떤지..


def recursion(n):
    # 기저사례
    if n == 1 or n == 0:
        return 1
    
    return n * recursion(n - 1)

N = int(input())

print(recursion(N))