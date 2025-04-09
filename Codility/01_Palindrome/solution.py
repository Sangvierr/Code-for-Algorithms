class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

def is_matched(open, close):
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)

def solution(S):
    s = Stack()
    for char in S:
        if char in "({[":
            s.push(char)
        elif char in ")}]":
            if s.is_empty():
                return 0
            top = s.pop()
            if not is_matched(top, char):
                return 0
    
    if s.is_empty():
        return 1
    else:
        return 0

print(solution("{[()()]}"))
print(solution("([)()]"))

# O(N)