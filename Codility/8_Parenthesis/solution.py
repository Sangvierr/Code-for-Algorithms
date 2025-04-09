def solution(string):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    # 처음부터 닫는 괄호면 짝을 맞출 수 없음
    if string[0] in [')', '}', ']']:
        return 0
    
    for s in string:
        # 여는 괄호면 스택에 추가
        if s in ['(', '{', '[']:
            stack.append(s)
        # 닫는 괄호면 짝이 맞는지 확인
        else:
            # 이미 스택이 비어있거나 찍이 안 맞으면 틀림
            if stack[-1] != mapping[s] or not stack:
                return 0
            
            stack.pop()
    
    # 스택에 남은 괄호가 없으면 짝이 맞음
    if not stack:
        return 1
    return 0

string = '({{[()]}})'
print(solution(string))

string = '({{[())]}})'
print(solution(string))

string = '}{}'
print(solution(string))
            