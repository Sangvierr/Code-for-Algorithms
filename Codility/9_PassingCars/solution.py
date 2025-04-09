def solution(A):
    west = 0
    total = 0
    
    # 끝에서부터 서쪽으로 가는 차량의 합계
    for car in reversed(A):
        if car == 1:
            west += 1
    
    # 동쪽으로 가는 차량을 만나면 서쪽으로 가는 차량의 합계와 더함
    for car in A:
        if car == 0:
            total += west
            if total > 1000000000:
                return -1
        else:
            west -= 1
                
    return total

A = [0, 1, 0, 1, 1]
print(solution(A))

A = [1, 0, 0, 0, 0]
print(solution(A))

# O(N)