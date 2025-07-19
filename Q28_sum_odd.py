# Sum of first N odd numbers.

n = int(input("Enter a Number: "))

sum = 0 
for i in range(1,n+1,2):          
    sum = sum + i 
print(sum)      