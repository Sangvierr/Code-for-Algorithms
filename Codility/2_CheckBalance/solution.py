def process_a(x:str):
    total=0
    for num in x:
        total+=int(num)
        
    return str(total)

def process_b(x:str):
    
    return str(abs(int(x[-1])-int(x[-2])))

def solution(balance):
    answer = ''
    answer+=balance[0]
    
    for i in range(1, len(balance)):
        if balance[i]=='A':
            answer+=process_a(answer[:i])
        elif balance[i]=='B': 
            answer+=process_b(answer[:i])
        else:
            answer+=balance[i]
            
    return answer

if __name__ == '__main__':
    balance = '512'
    print(solution(balance))

    balance = '5A2'
    print(solution(balance))

    balance = '55AA'
    print(solution(balance))

    balance = '55AAB'
    print(solution(balance))