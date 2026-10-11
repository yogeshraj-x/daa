# Program 5: Sum of cubes of first n natural numbers
# Formula: [n(n+1)/2]^2        Time: O(n)   Space: O(1)
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i ** 3
print("Sum of cubes using loop    =", total)
print("Sum of cubes using formula =", (n * (n + 1) // 2) ** 2)
