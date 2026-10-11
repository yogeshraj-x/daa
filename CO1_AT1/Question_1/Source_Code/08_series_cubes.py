# Program 8: Calculate 1^3 + 2^3 + 3^3 + ... + n^3
# Time complexity: O(n)   Space complexity: O(1)
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    print(i ** 3, end="" if i == n else " + ")
    total += i ** 3
print("\nSum =", total)
