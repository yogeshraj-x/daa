# Program 10: Display all prime numbers between 1 and n
# Uses trial division up to sqrt(num)
# Time complexity: O(n*sqrt(n))   Space complexity: O(1)
import math

n = int(input("Enter n: "))
print("Prime numbers:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
