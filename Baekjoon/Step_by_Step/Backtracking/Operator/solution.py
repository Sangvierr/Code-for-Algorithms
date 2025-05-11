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

backtracking(1, arr[0], plus, minus, multiply, divide) # 0이 아니라 1부터 해야 앞에 수랑 연산 가능
print(MAX, MIN)