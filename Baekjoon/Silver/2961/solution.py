import sys

T = int(sys.stdin.readline().rstrip())
S = []
B = []

for _ in range(T):
    s, b = map(int, sys.stdin.readline().rstrip().split())
    S.append(s)
    B.append(b)

# T개 중에서 n개를 뽑는 조합
def combinations(n, arr, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        return [new_arr]
    
    result = []
    for i in range(c, len(arr)):
        result.extend(combinations(n, arr, new_arr + [arr[i]], i + 1))
    return result

min_val = 1e9

for i in range(1, T+1):
    new_S = combinations(i, S, [], 0)
    new_B = combinations(i, B, [], 0)

    for j in range(len(new_S)):
        prod_S=1
        sum_B=0

        for k in range(i):
            prod_S *= new_S[j][k]
            sum_B += new_B[j][k]
            
        result = abs(prod_S - sum_B)

        if result < min_val:
            min_val = result

print(min_val)