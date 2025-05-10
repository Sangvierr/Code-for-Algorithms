# 2차원 M*N 배열을 시계 방향 90도, 반시계 방향 90도 회전
# 180, 270도는 90도 구현 후 반복하면 됨

M, N = map(int, input().strip().split()) # 행의 개수, 열의 개수
arr = [list(map(int, input().strip().split())) for _ in range(M)] # 직사각형

def clockwise_90(arr):
    m, n = len(arr), len(arr[0])

    temp = [[0]*M for _ in range(N)] # 행과 열을 바꿔줌

    for r in range(m):
        for c in range(n):
            temp[c][m-1-r] = arr[r][c]

    return temp

def counterclockwise_90(arr):
    m, n = len(arr), len(arr[0])

    temp = [[0]*M for _ in range(N)] # 행과 열을 바꿔줌

    for r in range(m):
        for c in range(n):
            temp[n-1-c][r] = arr[r][c]

    return temp
    
print(clockwise_90(arr))
print(counterclockwise_90(arr))