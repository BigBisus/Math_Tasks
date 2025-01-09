def next_permutation(perm):
    n = len(perm)
    i = n - 2

    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i == -1:
        return None
    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1

    perm[i], perm[j] = perm[j], perm[i]
    perm = perm[:i+1] + perm[i+1:][::-1]
    return perm

def generate_permutations(n):
    perm = list(range(1, n + 1))
    while perm:
        print(perm)
        perm = next_permutation(perm)

generate_permutations(5)
