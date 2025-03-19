n = 4  # 체스판 크기 (n x n)
pos = [-1] * n  # 각 열에서 퀸의 위치 (초기값 -1)
flag = [False] * n  # 각 행에 퀸을 배치했는지 체크

def print_board():
    """퀸이 배치된 결과를 출력"""
    print("퀸 배치 결과:", pos)

def place_queen(column):
    """column 번째 열에 퀸을 배치"""
    if column == n:  # 모든 열에 배치 완료
        print_board()
        return
     
    for row in range(n):  # 현재 column에 대해 모든 row 검사
        if not flag[row]:  # 이미 사용된 행이 아니면 배치 가능
            pos[column] = row  # 퀸 배치
            flag[row] = True  # 사용한 행 표시
            place_queen(column + 1)  # 다음 열로 이동
            flag[row] = False  # 백트래킹 (원래 상태로 되돌림)

place_queen(0)
