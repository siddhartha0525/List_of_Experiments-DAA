```python
# Factorial using Iterative and Recursive methods

# Iterative method
def iterative_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Recursive method
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)


# Input
n = int(input("Enter a number: "))

print("Factorial using Iterative method:", iterative_factorial(n))
print("Factorial using Recursive method:", recursive_factorial(n))
```
