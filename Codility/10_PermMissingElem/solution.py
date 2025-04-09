def solution(A):
    n = len(A)
    if n == 1:
        return None
    else:
        max_val = max(A)
        permute_list = [i for i in range(1, max_val+1)]
        
        for num in permute_list:
            if num not in A:
                break
        
        return num
    
A = [2, 3, 1, 5]
print(solution(A))

A = [1]
print(solution(A))

A = [1, 1, 1, 1, 3]
print(solution(A))

A = [i for i in range(1, 9999)] + [i for i in range(10000, 100000)]
print(solution(A))