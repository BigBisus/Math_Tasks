def generate_combinations(n, k):
    combination = list(range(1, k + 1))
    result = []

    while True:
        result.append(combination[:])
        for i in range(k - 1, -1, -1):
            if combination[i] < n - k + i + 1:
                break
        else:
            break
        combination[i] += 1
        for j in range(i + 1, k):
            combination[j] = combination[j - 1] + 1
    return result

n, k = 7, 4
combinations = generate_combinations(n, k)
for combo in combinations:
    print(combo)
