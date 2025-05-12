N, M = map(int, input().strip().split()) # 도시 크기, 고르는 최대 개수
arr = [list(map(int, input().strip().split())) for _ in range(N)] # 지도

homes=[] # 집의 좌표들
chickens=[] # 치킨집의 좌표들
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            homes.append([r, c])
        elif arr[r][c] == 2:
            chickens.append([r, c])

def combination(n, arr, new_arr, c):
    total=[]
    if len(new_arr) == n:
        total.append(new_arr)
        return total
    
    for i in range(c, len(arr)):
        total.extend(combination(n, arr, new_arr+[arr[i]], i+1))

    return total

chosen_chickens = combination(M, chickens, [], 0) # 3차원

total_chicken_distances = []
for chosen_chicken_set in chosen_chickens: # M개의 치킨집 좌표
    home2chicken = 0 # 전체 치킨 거리
    for hr, hc in homes:
        min_home2chicken = float('inf') # 각 집에서 가장 가까운 치킨집 거리 초기화
        for cr, cc in chosen_chicken_set:
            dist = abs(hr - cr) + abs(hc - cc) # 각 집과 치킨 집의 치킨 거리를 계산(모든 조합에 대해서)
            min_home2chicken = min(min_home2chicken, dist) # 그 중에서 최솟값만 치킨집으로 선택됨
        home2chicken += min_home2chicken # 치킨 거리에 한 집에서 최소 거리인 치킨 집의 치킨 거리 더함
    total_chicken_distances.append(home2chicken) # 모든 조합에 대한 치킨 거리 계산 후 append

print(min(total_chicken_distances)) # 모든 조합 중 사라지는 치킨집 조합 중 그 거리가 최소인 것