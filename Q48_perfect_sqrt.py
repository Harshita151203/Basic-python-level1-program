#  Check if number is perfect square.
n = int(input("Enter any number: "))
result = int(n**0.5)

if(result*result == n):
    print("Perfect Square")
else:
    print("Not a Perfect Square")

# ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

import math
n = int(input("Enter any number: "))
result  = math.isqrt(n)

if(result*result == n):
    print("Perfect Square")
else:
    print("Not a Perfect Square")