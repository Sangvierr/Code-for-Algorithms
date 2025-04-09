# nC3은 경우가 매우 많으니 정렬을 사용
def solution(A):
    sorted_list = sorted(A)
    
    last_three = sorted_list[-1] * sorted_list[-2] * sorted_list[-3]
    
    first_two_and_last_one = sorted_list[-1] * sorted_list[0] * sorted_list[1]
    
    return max(last_three, first_two_and_last_one)

# O(N * log(N))