from collections import deque

N, M = map(int, input().strip().split()) # 행,열
mal_r, mal_c, jjol_r, jjol_c = map(int, input().strip().split())
dir_guide = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def bfs():
    visited = [[0]*(M+1) for _ in range(N+1)]
    q = deque([(mal_r, mal_c, 0)])
    visited[mal_r][mal_c] = 1

    while q:
        r, c, cnt = q.popleft()

        if r == jjol_r and c == jjol_c:
            return cnt
        
        for dr, dc in dir_guide:
            nr = dr+r
            nc = dc+c

            if nr<1 or nc<1 or nr>N or nc>M: continue
            if visited[nr][nc]: continue

            q.append((nr, nc, cnt+1))
            visited[nr][nc] = 1

    return -1

print(bfs())