import sys

def heapify(arr, n, i): # 배열, 배열의 길이, 노드 인덱스
    """ 반복문을 사용하여 힙 속성을 유지하는 함수 """
    while True:
        largest = i  # 현재 노드를 가장 큰 값으로 가정
        left = 2 * i + 1  # 왼쪽 자식 노드 인덱스
        right = 2 * i + 2  # 오른쪽 자식 노드 인덱스
        # 왼쪽 자식이 존재하고, 현재 노드보다 크다면 largest 갱신
        if left < n and arr[left] > arr[largest]:
            largest = left
        # 오른쪽 자식이 존재하고, 현재 largest보다 크다면 largest 갱신
        if right < n and arr[right] > arr[largest]:
            largest = right