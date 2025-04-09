# def solution(A):
#    n = len(A)
#    min_sum = 10 ** 10
#    for i in range(1, n):
#        B = A[:i]
#        C = A[i:]
#        total = abs(sum(B)-sum(C))
       
#        min_sum = min(total, min_sum)
   
#    return min_sum

# A = [3, 5]
# print(solution(A))

# A = [3, 1, 2, 4, 3]
# print(solution(A))

# A = [-1000, -1000, -1000, -1000, -1000, 1000]
# print(solution(A))

# O(N^2)

# def solution(A):
#     n = len(A)
#     min_sum = 10 ** 10
#     total_sum = sum(A) # 전체 배열의 합에서 O(N)
#     for i in range(1, n):
#         left_sum = sum(A[:i]) # 리스트를 한번 더 만들어서 합하면 O(N)
#         rigth_sum = total_sum - left_sum
#         diff = abs(left_sum-rigth_sum)
        
#         min_sum = min(diff, min_sum)
    
#     return min_sum

# A = [3, 5]
# print(solution(A))

# A = [3, 1, 2, 4, 3]
# print(solution(A))

# A = [-1000, -1000, -1000, -1000, -1000, 1000]
# print(solution(A))

# O(N^2)

def solution(A):
    n = len(A)
    min_sum = 10**10
    left_sum = 0
    total_sum = sum(A)
    for i in range(1, n):
        left_sum += A[i-1]
        rigth_sum = total_sum - left_sum
        diff = abs(left_sum-rigth_sum)
        min_sum = min(diff, min_sum)
    
    return min_sum

A = [3, 5]
print(solution(A))

A = [3, 1, 2, 4, 3]
print(solution(A))

A = [-1000, -1000, -1000, -1000, -1000, 1000]
print(solution(A))

# O(N)