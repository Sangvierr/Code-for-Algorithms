def solution(indices, K):
    n = len(indices)
    # 각 폴드의 크기를 계산
    fold_size = n // K
    remainder = n % K
    
    # 각 폴드의 시작과 끝 인덱스를 계산하여 저장
    folds = []
    start = 0
    for i in range(K):
        size = fold_size + (1 if i < remainder else 0)
        folds.append(indices[start:start+size])
        start += size

    # 각 폴드를 테스트 세트로 사용하고 나머지를 훈련 세트로 사용하여 결과를 저장
    result = []
    for i in range(K):
        test_set = folds[i]
        training_set = []
        for j in range(K):
            if j != i:
                training_set.extend(folds[j])
        result.append([training_set, test_set])

    return result

# 예시 사용법
indices_example = [1, 2, 3]
K_example = 2
print(solution(indices_example, K_example))