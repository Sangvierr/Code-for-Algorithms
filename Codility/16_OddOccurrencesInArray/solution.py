def solution(A):
    result = 0
    for num in A:
        result = result ^ num # XOR
    
    return result

A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))

# O(N) or O(N*log(N))