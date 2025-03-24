# 이분탐색
N = int(input())

arr = sorted(list(map(int, input().split())))

M = int(input())

arr2 = list(map(int, input().split()))

def binary_search(n):
    l = 0
    r = len(arr) - 1

    while l <= r:
        c = (l + r) // 2

        if arr[c] == n:
            return arr[c]
        elif arr[c] < n:
            l = c + 1
        else:
            r = c - 1

    return None

for a in arr2:
    if binary_search(a):
        print("1")
    else: 
        print("0")

        