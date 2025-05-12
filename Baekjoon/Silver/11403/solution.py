# 경로 찾기
# 인접 행렬에서 사방으로 갈 수 있는 경로가 있는지 확인
# visited는 0으로 초기화 후 방문하면 1로 출력

from collections import deque

N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(x):
    q= deque([(x)])
    answer = [0]*N

    while q:
        cur_x = q.popleft()

        for i in range(N):
            if not answer[i] and arr[cur_x][i]:
                q.append(i)
                visited[x][i] = 1
                answer[i] = 1
        

for i in range(N):
    bfs(i)

for row in visited:
    print(*row)