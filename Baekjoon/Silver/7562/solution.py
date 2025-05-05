# 최단거리 bfs
# visited는 -1로 초기화 후 거리로 채움
# pop하면서 종료 조건 확인

from collections import deque

T = int(input())

for _ in range(T):
    L = int(input()) # 정사각형 한변의 길이
    cur_r, cur_c = map(int, input().strip().split()) # 나이트가 현재 있는 칸
    end_r, end_c = map(int, input().strip().split()) # 나이트가 이동하려고 하는 칸
    dir_guide = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited = [[-1]*L for _ in range(L)]
        visited[sr][sc] = 0

        while q:
            r, c = q.popleft()

            if (r, c) == (end_r, end_c):
                return visited[r][c]

            for dr, dc in dir_guide:
                nr=r+dr
                nc=c+dc

                if 0<=nr<L and 0<=nc<L and visited[nr][nc] == -1: # -1은 아직 방문 안 함!
                    q.append((nr, nc))
                    visited[nr][nc]=visited[r][c]+1

        return -1

    print(bfs(cur_r, cur_c))