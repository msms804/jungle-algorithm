pos = [0] * 4       # 각 열에서 퀸의 위치
flag = [False] * 4  # 각 행에 퀸을 배치했는지 체크

def put() -> None: 
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(4):
        print(f'{pos[i]:2}', end="")
    print()

def set(i : int) -> None:
    """각 열에 배치한 퀸의 위치의 출력"""
    for j in range(4):
        if not flag[j]:
            pos[i] = j
            if i == 3:
                put()            
            else:
                flag[j] = True
                set(i + 1)
                flag[j] = False

set(0)

