# Program 9: Check whether a number is prime
# Optimised: only test divisors up to sqrt(n)
# Time complexity: O(sqrt(n))   Space complexity: O(1)
import math

n = int(input("Enter a number: "))
is_prime = n >= 2
for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
