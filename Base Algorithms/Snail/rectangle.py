# 직사각형의 (0, 0)에서 시작
# 회오리 모양으로 외부부터 내부를 채워나감
# 우, 하, 좌, 상 방향으로 움직임

m, n = map(int, input().strip().split()) # 행과 열의 길이
arr = [[0]*n for _ in range(m)]
dir_guide = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상
dir_idx = 0 # 먼저 오른쪽으로 가다가 못 가면 다음 인덱스로 넘기는 용
r, c = 0, 0

arr[r][c] = 1

for i in range(2, m*n+1):
    dr, dc = dir_guide[dir_idx]
    nr, nc = r+dr, c+dc

    if 0<=nr<m and 0<=nc<n and arr[nr][nc] == 0: # 범위 내에 있고, 다음 칸을 아직 안 감
        r, c = nr, nc
        arr[r][c] = i
    else:
        dir_idx = (dir_idx+1)%4
        dr, dc = dir_guide[dir_idx]
        nr, nc = r+dr, c+dc
        r, c = nr, nc
        arr[r][c] = i

for row in arr:
    print(' '.join(map(str, row)))