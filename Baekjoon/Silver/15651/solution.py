import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [i for i in range(1, N+1)]

def combinations_with_replacement(n, new_arr):
    # 순서 상관 X, 중복
    if len(new_arr) == n:
        print(*new_arr)
        return
    for i in range(len(arr)):
        combinations_with_replacement(n, new_arr + [arr[i]])

combinations_with_replacement(M, [])