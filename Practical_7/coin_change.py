```python
# Coin Change (Making Change) using Dynamic Programming

def coin_change(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Calculate minimum coins
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

result = coin_change(coins, amount)

if result == -1:
    print("Amount cannot be made with given coins.")
else:
    print("Minimum number of coins:", result)
```
