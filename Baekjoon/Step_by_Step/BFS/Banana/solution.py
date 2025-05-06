# 주변 상우하좌 4군데를 탐색
# open 가능하다면 큐에 삽입, 인덱스도 저장
# open 가능한 곳의 바나나 개수 누적합, cnt도 누적합
# 재할당할 필요가 사라지면 종료

from collections import deque

N, L, R = map(int, input().strip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split())))
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def bfs(r, c, visited):
    q = deque([(r, c)])
    visited[r][c] = 1

    # r, c를 열어야 함
    current_open = [(r, c)]
    current_sum = arr[r][c]
    current_cnt = 1

    while q:
        row, col = q.popleft()

        for dr, dc in dir_guide:
            nr=dr+row
            nc=dc+col

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]: # 갈 수 있는 범위 내에서 아직 방문 안 함
                diff = abs(arr[nr][nc] - arr[row][col])
                if L<=diff<=R:
                    visited[nr][nc]=1
                    current_open.append((nr, nc))
                    current_sum+=arr[nr][nc]
                    current_cnt+=1
                    q.append((nr, nc))

    return current_open, current_sum, current_cnt

answer=0
while True:
    visited=[[0]*N for _ in range(N)]
    reallocate=False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                current_open, current_sum, current_cnt = bfs(r, c, visited)

                if len(current_open) > 1: # 오픈된 곳이 있음
                    new_banana = current_sum // current_cnt

                    for row, col in current_open:
                        arr[row][col] = new_banana
                        reallocate=True

    if not reallocate:
        break

    answer+=1

print(answer)