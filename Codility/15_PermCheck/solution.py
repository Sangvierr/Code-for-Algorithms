def solution(A):
    length = len(A)
    
    A_sorted = sorted(A)
    new_list = [i+1 for i in range(length)]
    
    hit = 0
    for i in range(length):
        if A_sorted[i] != new_list[i]:
            hit += 1
    
    if hit != 0:
        return 0
    else:
        return 1
        
A = [1, 2, 3, 4, 6]
print(solution(A))

A = [1, 2, 3, 4, 5, 6]
print(solution(A))

A = [1, 2, 3, 3]
print(solution(A))

# O(N) or O(N * log(N))