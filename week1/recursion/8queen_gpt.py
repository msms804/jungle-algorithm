n = 4
pos = [-1] * n
flag_row = [False] * n
flag_diag1 = [False] * (2 * n - 1)  # "/" 방향 대각선 (row + col)
flag_diag2 = [False] * (2 * n - 1)  # "\" 방향 대각선 (row - col + n - 1)

def print_board():
    print("퀸 배치 결과:", pos)

def place_queen(column):
    if column == n:
        print_board()
        return

    for row in range(n):
        if not flag_row[row] and not flag_diag1[row + column] and not flag_diag2[row - column + n - 1]:
            pos[column] = row
            flag_row[row] = flag_diag1[row + column] = flag_diag2[row - column + n - 1] = True
            place_queen(column + 1)
            flag_row[row] = flag_diag1[row + column] = flag_diag2[row - column + n - 1] = False 

place_queen(0)
