def increase(A, i):
    A[i] += 1
    
    return A 

def solution(N, A):
    new_list = [0] * N
    for num in A:
        if num == N+1:
            new_list = [max(new_list)] * N
        else:
            new_list = increase(new_list, num-1)
            
    return new_list

A = [3, 4, 4, 6, 1, 4, 4]
N = 5
print(solution(N, A))

# O(M * N)