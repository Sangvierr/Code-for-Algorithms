# l: 리스트, 인덱스는 x축 좌표이고 값은 y축 좌표
# y: 기준이 되는 y축 값

def solution(l, y):
    
    ll = list(map(lambda x: x - y, l))
    
    count = 0
    for i in range(len(l)-1):
        if ll[i] * ll[i+1] <= 0:
            count += 1
    
    return count

if __name__ == '__main__':
    print(solution([-1, 2, 3, 4, 5], 0))
    print(solution([-1, 2, 3, 4, 5], -2))
    print(solution([-3, 3, 0, 3, -3], 2))