def solution(A):
    n = len(A)
    total_sum = (n+1)*(n+2) // 2 # 부동소수점 없애기 위해서 몫으로 설정
    array_sum = sum(A)
    num = total_sum - array_sum
    return num
    
A = [2, 3, 1, 5]
print(solution(A))

A = [1]
print(solution(A))

A = [1, 1, 1, 1, 3]
print(solution(A))

A = [i for i in range(1, 9999)] + [i for i in range(10000, 100000)]
print(solution(A))

A = []
print(solution(A))

A = [1, 2, 3, 4]
print(solution(A))

# O(N) or O(N * log(N))
