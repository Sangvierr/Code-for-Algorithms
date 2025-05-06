N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split())))

result = 1e10 # 작은 값을 찾아야 하므로 큰 값으로 초기화
visited = [0]*N

def backtracking(idx, a):
    global result

    # 계속 돌면서 절반에 도달했다면(절반은 visit 했고, 나머지 절반은 아님)
    if a == N//2:
        start_team = 0
        link_team = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_team += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link_team += arr[i][j]

        result = min(result, abs(start_team-link_team))

        return
    
    else:
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = 1
                backtracking(i+1, a+1)
                visited[i] = 0

backtracking(0, 0)
print(result)