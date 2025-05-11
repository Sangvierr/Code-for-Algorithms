from collections import deque

N = int(input()) # 전체 컴퓨터의 개수(100이하)
NP = int(input()) # 연결된 컴퓨터 쌍의 개수
lst = [] # 연결된 컴퓨터 네트워크
for _ in range(NP):
    lst.extend(list(map(int, input().strip().split())))

# 인접 리스트
adj_lst={}
for i in range(0, len(lst), 2):
    u = lst[i]
    v = lst[i+1]

    if u not in adj_lst:
        adj_lst[u] = []
    adj_lst[u].append(v)

    if v not in adj_lst:
        adj_lst[v] = []
    adj_lst[v].append(u)

# BFS
def bfs(start_node):
    q = deque([start_node])
    visited = [0] * (N+1) # 100 이하이기 때문에
    visited[start_node] = 1
    cnt=0 # 첫노드는 무조건 방문

    while q:
        cur_node = q.popleft()

        if cur_node in adj_lst: # 연결 정보가 없으면 넘어가야 함(이 부분에서 런타임 에러 발생 주의)
            for neighbors in adj_lst[cur_node]:
                if not visited[neighbors]: # 인접한 이웃 노드 확인
                    q.append(neighbors)
                    visited[neighbors] = 1
                    cnt+=1

    return cnt

print(bfs(1))