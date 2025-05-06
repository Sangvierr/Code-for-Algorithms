# 백트래킹을 통해서 구현
# 중복순열은 N개 중에서 중복 허용해서 M개를 선택해서 나열
# Ex) 1부터 5 중에서 중복 있이 2개를 나열하는 경우 => (1, 1) 가능
# 뽑고 나열까지 하기 때문에 (1, 2)와 (2, 1)은 다른 것

def n_rpl_permute_m(n, arr, new_arr):
    '''
    n: 몇개를 뽑을건지
    arr: 뽑는 대상이 되는 숫자 리스트
    new_arr: 결과를 담을 새로운 리스트 
    '''

    if len(new_arr) == n:
        print(*new_arr)
        return
    
    for i in range(len(arr)):
        n_rpl_permute_m(n, arr, new_arr+[arr[i]])

N, M = map(int, input().split())
arr = [i+1 for i in range(N)]

n_rpl_permute_m(M, arr, [])