# 2차원 N*N 배열을 시계 방향으로 90도, 반시계 방향으로 90도 회전
# 180, 270도는 90도 구현 후 반복하면 됨
# 번외) 좌우 대칭, 상하 대칭도 있음

N = int(input()) # 사각형의 크기
arr = [list(map(int, input().strip().split())) for _ in range(N)] # 정사각형

def clockwise_90(arr):
    n = len(arr) # 한 변 길이

    temp = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            temp[c][n-1-r] = arr[r][c] # 돌리기 전 행과 돌린 후 열은 고정 => 두개 더하면 n-1

    return temp

def counterclockwise_90(arr):
    n = len(arr) # 한 변 길이

    temp = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            temp[n-1-c][r] = arr[r][c]

    return temp

print(clockwise_90(arr))
print(counterclockwise_90(arr))