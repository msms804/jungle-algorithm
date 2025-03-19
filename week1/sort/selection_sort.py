# 단순 선택 정렬
a = [6, 4, 8, 3, 1, 9, 7]

from typing import MutableSequence 

def selection_sort(a: MutableSequence) -> None:
    """단순선택정렬"""
    n = len(a)

    for i in range(n - 1):
        min = i # 정렬할 부분에서 가장 작은 원소의 인덱스

        for j in range(i + 1, n):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

selection_sort(a)

print(a)
