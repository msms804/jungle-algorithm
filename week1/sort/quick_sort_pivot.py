from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬 (피벗을 첫 번째 원소로 선택)"""
    pl = left  # 피벗 바로 다음 요소부터 시작
    pr = right
    x = a[left]  # 피벗을 첫 번째 원소로 설정

    print(f'a[{left}] ~ a[{right}] :', *a[left : right + 1])
    while pl <= pr:
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print("퀵 정렬을 수행합니다.")
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)

    print("오름차순으로 정렬했습니다.")

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
