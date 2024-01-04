# Brute Force
def knapsack_brute(v, w, n, W):
    # Base Case: No items left or no remaining capacity in the knapsack
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than the knapsack capacity W,
    # then this item cannot be included in the optimal solution
    if w[n - 1] > W:
        return knapsack_brute(v, w, n - 1, W)

    # Return the maximum of two cases:
    # 1. nth item included
    # 2. not included
    else:
        return max(v[n - 1] + knapsack_brute(v, w, n - 1, W - w[n - 1]), knapsack_brute(v, w, n - 1, W))
    
    # Memoization
def knapsack_memo(v, w, n, W, memo):
    # Check if the value is already computed
    if (n, W) in memo:
        return memo[(n, W)]

    # Base Case: No items left or no remaining capacity in the knapsack
    if n == 0 or W == 0:
        return 0

    # If the weight of the nth item is more than the knapsack capacity W,
    # this item cannot be included in the optimal solution
    if w[n - 1] > W:
        memo[(n, W)] = knapsack_memo(v, w, n - 1, W, memo)
    else:
        # Compute the value with and without the nth item and store the maximum
        memo[(n, W)] = max(v[n - 1] + knapsack_memo(v, w, n - 1, W - w[n - 1], memo),
                           knapsack_memo(v, w, n - 1, W, memo))
    return memo[(n, W)]

# Wrapper function
def knapsack_with_memo(v, w, W):
    memo = {}
    return knapsack_memo(v, w, len(v), W, memo)

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

# Calculate the maximum value using memoization
max_value_memo = knapsack_with_memo(values, weights, W)
print(max_value_memo)

# Tabulation
def knapsack_tabulation(v, w, W):
    n = len(v)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

# Calculate the maximum value that can be put in the knapsack using tabulation
max_value_tabulation = knapsack_tabulation(values, weights, W)
print(max_value_tabulation)


