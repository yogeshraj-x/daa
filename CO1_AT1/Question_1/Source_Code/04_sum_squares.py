# Program 4: Sum of squares of first n natural numbers
# Formula: n(n+1)(2n+1)/6      Time: O(n)   Space: O(1)
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i * i
print("Sum of squares using loop    =", total)
print("Sum of squares using formula =", n * (n + 1) * (2 * n + 1) // 6)
