def check(string):
    stack=[]
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(': # 스택이 비었거나 마지막이랑 일치 안 함
                return 'no'
            stack.pop()
        elif s ==']': # 스택이 비었거나 마지막이랑 일치 안 함
            if not stack or stack[-1] != '[':
                return 'no'
            stack.pop()

    if not stack: # 마지막에 비어있다면 쌍 맞음
        return "yes"
    else: # 뭔가가 남아있으면 쌍 아님
        return 'no'

import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    filtered_line = ''.join(char for char in line if char in '()[]')

    if not filtered_line:
        print('yes')
    else:
        result = check(filtered_line)
        print(result)