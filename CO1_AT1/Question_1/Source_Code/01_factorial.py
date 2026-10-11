# Program 1: Factorial of a number using a for loop
# Time complexity: O(n)   Space complexity: O(1)
n = int(input("Enter n: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"Factorial of {n} =", fact)
