def findJudge(n, trust):
    if n == 1:
        return 1 if not trust else -1

    trust_count = [0] * (n + 1)
    trusted_by_count = [0] * (n + 1)

    for a, b in trust:
        trust_count[b] += 1
        trusted_by_count[a] += 1

    for person in range(1, n + 1):
        if trust_count[person] == n - 1 and trusted_by_count[person] == 0:
            return person

    return -1

# Test case
n = 3
trust = [[1, 3], [2, 3]]

# Call the function
town_judge = findJudge(n, trust)

# Print the result
print(f"The town judge is: {town_judge}")