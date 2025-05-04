from collections import deque

M, N = map(int, input().split()) # 세로 M, 가로 N
A = [list(map(int, input().split())) for _ in range(M)]
sr, sc, sd = map(lambda x:int(x)-1, input().split())
er, ec, ed = map(lambda x:int(x)-1, input().split())
visited = [[[0]*4 for _ in range(N)] for _ in range(M)]
dir_guide = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동, 서, 남, 북

def bfs():
    q = deque([(sr, sc, sd, 0)])
    visited[sr][sc][sd] = 1

    while q:
        r, c, d, cnt = q.popleft()

        if (r, c, d) == (er, ec, ed):
            print(cnt)
            return
        
        # Go k=1, 2, 3
        ndr, ndc = dir_guide[d]
        for i in range(1, 4):
            nr=r+ndr*i
            nc=c+ndc*i

            if nr<0 or nr>=M or nc<0 or nc>=N: break # 해당 칸을 넘어가는게 아니라 벽을 만나면 아예 못 감감
            if A[nr][nc]: break
            if visited[nr][nc][d]: continue     
            
            q.append((nr, nc, d, cnt+1))
            visited[nr][nc][d] = 1
        
        nds = (0, 1) if d>=2 else (2, 3)
        for nd in nds:
            if visited[r][c][nd]: continue
            q.append((r, c, nd, cnt+1))
            visited[r][c][nd] = 1

bfs()