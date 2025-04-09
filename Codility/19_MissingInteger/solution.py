def solution(A):
    seen = set()
    
    for num in A:
        if num > 0:
            seen.add(num)
            
    small = 1
    
    while small in seen:
        small += 1
    
    return small
            

A = [1, 3, 6, 4, 1, 2] 
print(solution(A)) # 5

A = [1, 2, 3]
print(solution(A)) # 4

A = [-1, 1, 2]
print(solution(A)) # 3

A = [i for i in range(1, 1000)]
print(solution(A)) # 1000

A = [-1, -2, -3]
print(solution(A)) # 1

# O(N) or O(N * log(N))