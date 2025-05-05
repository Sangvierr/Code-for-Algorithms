# 주변 4칸을 상우하좌 순서로 돌면서 open 할 곳을 탐색
# open할 곳은 큐에 삽입
# 분배할 바나나 개수 계산
# 분배할 바나나 개수 업데이트

from collections import deque

N, L, R = map(int, input().strip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split())))
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def bfs(r, c, visited):
    q = deque([(r, c)])
    visited[r][c]=1
    current_idx = [(r, c)] # open으로 연결한 인덱스
    current_sum = arr[r][c] # open한 애들의 바나나 개수 합
    current_cnt = 1 # open한 개수

    while q:
        row, col = q.popleft()

        for dr, dc in dir_guide:
            nr=dr+row
            nc=dc+col

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                diff = abs(arr[nr][nc]-arr[row][col])
                if L <= diff <= R:
                    visited[nr][nc] = 1
                    current_idx.append((nr, nc)) # 연결 완료
                    current_sum+=arr[nr][nc] # 바나나 덧셈 완료
                    current_cnt+=1 # open 개수 더하기 완료
                    q.append((nr, nc)) # 행, 열, 개수
    
    return current_idx, current_sum, current_cnt

answer=0
while True:
    visited = [[0]*N for _ in range(N)]
    reallocate=False

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                current_idx, current_sum, current_cnt = bfs(r, c, visited)

                if current_cnt > 1: # 만약 open 된 곳이 있다면
                    new_banana = current_sum // current_cnt

                    for row, col in current_idx:
                        arr[row][col] = new_banana
                    reallocate=True
        
    if not reallocate:
        break

    answer+=1

print(answer)