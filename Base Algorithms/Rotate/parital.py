# N*N 2차원 배열이 주어졌을 때, 특정 부분만 시계/반시계 방향으로 90도 회전
# 회전하는 인덱스만 따로 회전하고, 나머지 부분은 그냥 할당
# 180, 270도는 90도 구현 후 반복하면 됨

N = int(input()) # 사각형의 크기
arr = [list(map(int, input().strip().split())) for _ in range(N)] # 정사각형
sr, sc = map(int, input().strip().split()) # 시작 행, 열
length = int(input()) # 시작 행, 열로부터 몇칸까지 회전 대상

def partial_clockwise_90(sr, sc, length, arr):
    n = len(arr)

    temp = [[0]*N for _ in range(N)]

    for r in range(n):
        for c in range(n):
            if r in range(sr, sr+length) and c in range(sc, sc+length):
                temp[c][n-1-r] = arr[r][c]
            else:
                temp[r][c] = arr[r][c]

    return temp

def partial_counterclockwise_90(sr, sc, length, arr):
    n = len(arr)

    temp = [[0]*N for _ in range(N)]

    for r in range(n):
        for c in range(n):
            if r in range(sr, sr+length) and c in range(sc, sc+length):
                temp[n-1-c][r] = arr[r][c]
            else:
                temp[r][c] = arr[r][c]

    return temp


print(partial_clockwise_90(sr, sc, length, arr))
print(partial_counterclockwise_90(sr, sc, length, arr))