# Find LCM of two numbers.

import math
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

lcm = (a*b)//math.gcd(a, b)
print(f"LCM is : {lcm}")