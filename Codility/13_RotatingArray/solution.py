def solution(A, K):
    length = len(A)
    if length == 0:
        return A
    else:
        K = K % length
        new_arr = [0] * length
        for idx, num in enumerate(A):
            new_idx = (idx+K) % length
            new_arr[new_idx] = num
                
    return new_arr

A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))

A = [0, 0, 0]
K = 1
print(solution(A, K))

A = [1, 2, 3, 4]
K = 4
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))

A = [0, 0, 0]
K = 1
print(solution(A, K))

A = []
K = 4
print(solution(A, K))

A = [0, 1, 2, 3, 4, 5]
K = 8
print(solution(A, K))

