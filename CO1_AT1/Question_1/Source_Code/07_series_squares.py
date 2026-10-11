# Program 7: Calculate 1^2 + 2^2 + 3^2 + ... + n^2
# Time complexity: O(n)   Space complexity: O(1)
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    print(i ** 2, end="" if i == n else " + ")
    total += i ** 2
print("\nSum =", total)
