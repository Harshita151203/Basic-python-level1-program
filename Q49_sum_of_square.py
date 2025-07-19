# Sum of squares of first N numbers.

# using for loop :
n = int(input("Enter a Number: "))
sum = 0
for i in range(1,n+1):     
    sum += i**2
print(sum)


# using while loop :
n = int(input("Enter a Number: "))
sum = 0      
i = 1
while(n>=i):
    sum = sum + i**2
    i = i+1
print(sum)