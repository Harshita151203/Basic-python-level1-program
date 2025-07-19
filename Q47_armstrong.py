# Check if number is Armstrong number.

n = int(input("Emter any number: "))
dig = len(str(n))
total = 0

for i in str(n):
    total += int(i)**dig

if(n == total):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
