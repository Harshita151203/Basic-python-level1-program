# Print sum of digits of a number.

n = int(input("Enter a Number: "))

i = 1
sum = 0
while(i<=n):
    sum = sum + i
    i = i+1
print(sum)