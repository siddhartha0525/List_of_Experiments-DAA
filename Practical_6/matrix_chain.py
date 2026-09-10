```python
# Matrix Chain Multiplication using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1

    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


# Input
n = int(input("Enter number of matrices: "))

print("Enter dimensions of matrices:")
p = list(map(int, input().split()))

# Calculate minimum multiplication cost
result = matrix_chain_order(p)

print("Minimum number of scalar multiplications:", result)
```
