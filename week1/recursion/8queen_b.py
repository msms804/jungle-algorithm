pos = [0] * 3

def put() -> None: 
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(3):
        print(f'{pos[i]:2}', end="")
    print()

def set(i: int) -> None:
    """i 열에 퀸을 배치"""
    for j in range(3):
        pos[i] = j
        if i == 2:
            put()
        else: 
            set(i + 1)