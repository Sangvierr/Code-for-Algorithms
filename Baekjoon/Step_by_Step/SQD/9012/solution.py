def check(string):
    stack=[]
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack: # 스택이 비어있다면 쌍 아님
                return 'NO'
            else:
                if stack[-1] == '(':
                    stack.pop()
                else: # ')'가 들어있다면 쌍 아님
                    return 'NO'
    if not stack: # 마지막에 비어있다면 쌍 맞음
        return "YES"
    else: # 뭔가가 남아있으면 쌍 아님
        return 'NO'


T = int(input())

for _ in range(T):
    string = input()
    print(check(string))