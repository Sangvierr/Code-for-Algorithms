# S : LILLYBILLYBOO
# L : [‘BILL’, ‘MARIA’, ‘LILLY’]

def solution(S, L):
    S_dict = dict()
    
    for s in S:
        if s not in S_dict.keys():
            S_dict[s] = 1
        else:
            S_dict[s] += 1
    
    total_max = 0
    for name in L:
        L_dict = dict()
        for l in name:
            if l not in L_dict.keys():
                L_dict[l] = 1
            else:
                L_dict[l] += 1
        
        current = 0
        temp = 10**10
        for c in L_dict:
            if c in S_dict:
                current = S_dict[c]
                temp = min(current, temp)
        
        total_max = max(temp, total_max)
   
    return temp


S = 'LILLYBILLYBOO'
L = ['BILL', 'MARIA', 'LILLY']
print(solution(S, L))

S = "abracadabra"
L = ["abba", "cad"]
print(solution(S, L))

S = 'abcabcabcabcc'
L = ['abc', 'cba']
print(solution(S, L))