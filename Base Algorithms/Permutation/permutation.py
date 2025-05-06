# 백트래킹을 통해서 구현
# 순열은 N개 중에서 중복 없이 M개를 선택해서 나열
# Ex) 1부터 5 중에서 중복 없이 2개를 나열하는 경우 => (1, 1) 불가능
# 뽑고 나열까지 하기 때문에 (1, 2)와 (2, 1)은 다른 것

def n_permute_m(n, arr, new_arr, visited):
    '''
    n: 몇개를 뽑을건지
    arr: 뽑는 대상이 되는 숫자 리스트
    new_arr: 결과를 담을 새로운 리스트 
    visited: 각 숫자가 현재 순열에 포함되었는지 여부(중복 여부 확인)
    '''

    if len(new_arr) == n:
        print(*new_arr)
        return
    
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            n_permute_m(n, arr, new_arr+[arr[i]], visited)
            visited[i] = 0 # 백트래킹 완료 후에는 다시 원상 복구(다음 탐색을 위해)

N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
visited = [0] * N

n_permute_m(M, arr, [], visited)