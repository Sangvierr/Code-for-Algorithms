def solution(A):
    sort_list = sorted(A)
    n = len(sort_list)
    
    for i in range(0, n-2):
        if sort_list[i] + sort_list[i+1] > sort_list[i+2]:
            return 1
    
    return 0
        
A = [10, 2, 5, 1, 8, 20]
print(solution(A))

A = [10, 50, 5, 1]
print(solution(A))

# O(N * log(N)