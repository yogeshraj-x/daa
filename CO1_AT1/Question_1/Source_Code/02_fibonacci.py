# Program 2: Fibonacci series up to n terms
# Time complexity: O(n)   Space complexity: O(1)
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
