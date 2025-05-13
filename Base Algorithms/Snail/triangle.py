# 삼각형의 높이 N을 입력 받아 삼각형을 순서대로 채우기
# 맨 위부터 시작
# 방향: 대각선, 좌, 상

n = int(input()) # 한변 길이
arr = [[0]*i for i in range(1, n+1)]
dir_guide = [(1, 1), (0, -1), (-1, 0)] # 대각선, 좌, 상
dir_idx = 0
r, c = 0, 0

arr[r][c] = 1

for i in range(2, ((n+1)*(n))//2+1):
    dr, dc = dir_guide[dir_idx]
    nr, nc = r+dr, c+dc

    if 0<=nr<n and 0<=nc<n and arr[nr][nc]==0:
        r,c=nr,nc
        arr[r][c]=i
    else:
        dir_idx=(dir_idx+1)%3
        dr, dc = dir_guide[dir_idx]
        nr, nc = r+dr, c+dc
        r,c=nr,nc
        arr[r][c]=i

for row in arr:
    print(' '.join(map(str, row)))