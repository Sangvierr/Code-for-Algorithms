N = int(input()) # 숫자 개수
arr=list(map(int, input().split())) # n개의 정수
plus, minus, multiply, divide = map(int, input().strip().split()) # 연산자 개수

MIN = float('inf')
MAX = float('-inf')

def backtracking(idx, result, plus, minus, multiply, divide):
    global MIN, MAX

    if idx == N:
        MIN = min(MIN, result)
        MAX = max(MAX, result)
        return

    if plus > 0:
        backtracking(idx+1, result+arr[idx], plus-1, minus, multiply, divide)
    if minus > 0:
        backtracking(idx + 1, result-arr[idx], plus, minus-1, multiply, divide)
    if multiply > 0:
        backtracking(idx + 1, result * arr[idx], plus, minus, multiply-1, divide)
    if divide > 0:
        if result < 0:
            backtracking(idx + 1, -(-result // arr[idx]), plus, minus, multiply, divide-1)
        else:
            backtracking(idx + 1, result // arr[idx], plus, minus, multiply, divide - 1)

backtracking(1, arr[0], plus, minus, multiply, divide) # 첫번째 숫자 arr[0] 이후의 숫자와 계산하려면 idx는 1
print(MAX, MIN)