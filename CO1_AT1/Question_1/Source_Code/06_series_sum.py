# Program 6: Generate 1 + 2 + 3 + ... + n and calculate its sum
# Time complexity: O(n)   Space complexity: O(1)
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    print(i, end="" if i == n else " + ")
    total += i
print("\nSum =", total)
