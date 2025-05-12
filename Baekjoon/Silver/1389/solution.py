# 인접리스트로 입력값을 정의
# BFS로 풀되, bfs(1)부터 bfs(N)까지 반복 후 최솟값 출력
# visited는 0으로 초기화 후 방문 여부만 표시(함수 안에서)

from collections import deque

N, M = map(int, input().strip().split()) # 유저의 수, # 친구 관계
arr = []
for _ in range(M):
    arr.append(list(map(int, input().strip().split())))

adj_lst={}
for u, v in arr:
    if u not in adj_lst:
        adj_lst[u] = []
    adj_lst[u].append(v)

    if v not in adj_lst:
        adj_lst[v] = []
    adj_lst[v].append(u)

def bfs(start_node):
    q = deque([(start_node, 0)])
    visited = [0]*(N+1)
    visited[start_node]=1
    CNT = 0

    while q:
        cur_node, cnt = q.popleft()
        CNT+=cnt

        for naver in adj_lst[cur_node]:
            if not visited[naver]:
                q.append((naver, cnt+1))
                visited[naver]=1
    
    return CNT

MIN = float('inf')
idx = float('inf')
for i in range(1, N+1):
    val = bfs(i)
    if val < MIN:
        MIN = val
        idx=i

print(idx)