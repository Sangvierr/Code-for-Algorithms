# 백트래킹을 통해서 구현
# 조합은 N개 중에서 M개를 뽑을 때 한 원소를 여러 번 뽑을 수 없음
# Ex) 1부터 5 중에서 중복을 허용하여 2개를 뽑는 경우 => (1, 1) 불가능
# 단, 뽑기만 하기 때문에 (1, 2)와 (2, 1)은 동일

def n_choose_m(n, arr, new_arr, c):
    '''
    n: 몇개를 뽑을건지
    arr: 뽑는 대상이 되는 숫자 리스트
    new_arr: 결과를 담을 새로운 리스트
    c: 현재 인덱스(중복 아닌 인덱스 넘기면서 사용)
    '''

    if len(new_arr) == n:
        print(*new_arr)
        return
    
    for i in range(c, len(arr)):
        n_choose_m(n, arr, new_arr+[arr[i]], i+1)

N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
new_arr = []

n_choose_m(M, arr, new_arr, 0)