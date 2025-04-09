def solution(X, A):
    reached = [False] * (X+1)
    covered_position = 0
    
    for sec, position in enumerate(A):
        if position <= X and not reached[position]:
            reached[position] = True
            covered_position += 1
        
            if covered_position == X:
                return sec
    
    return -1

X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(X, A))
