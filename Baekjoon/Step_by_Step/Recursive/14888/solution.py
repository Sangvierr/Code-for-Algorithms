N = int(input().strip()) # 수의 개수
numbers = list(map(int, input().strip().split())) # 수
plus, minus, multiply, divide = map(int, input().strip().split()) # 연산자 개수

MAX = -1e10
MIN = 1e10

def backtracking(idx, result, plus, minus, multiply, divide):
    global MAX, MIN

    if idx == N: # 마지막 확인 후 최대/최소 갱신
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    
    if plus > 0:
        backtracking(idx+1, result+numbers[idx], plus-1, minus, multiply, divide)
    if minus > 0:
        backtracking(idx+1, result-numbers[idx], plus, minus-1, multiply, divide)
    if multiply > 0:
        backtracking(idx+1, result*numbers[idx], plus, minus, multiply-1, divide)
    if divide > 0:
        if result < 0:
            backtracking(idx+1, -(-result // numbers[idx]), plus, minus, multiply, divide-1) # 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼
        else:
            backtracking(idx+1, result//numbers[idx], plus, minus, multiply, divide-1)

backtracking(1, numbers[0], plus, minus, multiply, divide)

print(MAX)
print(MIN)