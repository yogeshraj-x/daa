# Program 3: Sum of first n natural numbers (loop method + formula check)
# Time complexity: O(n) for loop, O(1) for formula   Space complexity: O(1)
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum using loop    =", total)
print("Sum using formula =", n * (n + 1) // 2)
