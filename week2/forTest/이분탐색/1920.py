import sys

N = int(sys.stdin.readline())

arr1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()

def binary_search(a):
    l = 0
    r = len(arr1) - 1
    while l <= r:
        mid = (l + r) // 2

        if arr1[mid] == a:
            return 1            
        elif a > arr1[mid]:
            l = mid + 1
        else:
            r = mid - 1  

for a in arr2:
    if binary_search(a):
        print(1)
    else: 
        print(0)