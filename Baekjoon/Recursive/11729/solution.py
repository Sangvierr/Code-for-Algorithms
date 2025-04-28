import sys

N = int(sys.stdin.readline().rstrip())

# 1단계. (n-1)개를 0번부터 1번까지로 옮김
# 2단계. (1)개를 0번부터 2번까지로 옮김
# 3단계. (n-1)개를 1번부터 2번까지로 옮김

def move_hanoi(n, start, end):
    if n == 1:
        print(start, end) # 원판이 1개라면, 처음에서 끝으로 옮겨주면 끝
        return
    
    move_hanoi(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    move_hanoi(n-1, 6-start-end, end) # 3단계

print((2**N)-1)
move_hanoi(N, 1, 3)