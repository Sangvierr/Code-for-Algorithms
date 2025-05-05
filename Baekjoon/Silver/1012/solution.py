# 인접한 1의 개수 찾기
# => bfs
# => visited는 0로 초기화 + 방문하면 1로 바꾸기

from collections import deque

T = int(input()) # 테스트 케이스의 개수

for _ in range(T):
    M, N, K = map(int, input().strip().split()) # 가로, 세로, 개수

    arr = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int,  input().strip().split())
        arr[y][x] = 1

    dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

    visited = [[0]*M for _ in range(N)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = 1
        cnt=1

        while q:
            r, c = q.popleft()
        
            for dr, dc in dir_guide:
                nr=dr+r
                nc=dc+c

                if nr<0 or nc<0 or nr>=N or nc>=M: continue
                if visited[nr][nc]: continue
                if arr[nr][nc] == 0: continue

                q.append((nr, nc))
                visited[nr][nc] = 1
                cnt+=1

        return 1

    total = []
    for c in range(M):
        for r in range(N):
            if visited[r][c] == 0 and arr[r][c] == 1:
                total.append(bfs(r, c))

    print(len(total))