# def solution(A, B, K):
#     range_list = [i for i in range(A, B+1)]
#     TF_list = [num for num in range_list if num % K == 0]
    
#     return len(TF_list)

# A = 6
# B = 11
# K = 2
# print(solution(A, B, K))
        
# 시간 복잡도가 높음

def solution(A, B, K):
    if A % K == 0:
        start = A
    else:
        start = A + (K - A % K)
    
    if B % K == 0:
        end = B
    else:
        end = B - (B % K)
    
    if start > end:
        return 0
    else:
        return (end - start) // K + 1
    
A = 6
B = 11
K = 2
print(solution(A, B, K))

# O(1)