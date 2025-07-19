# Sum of cubes of first N numbers.  

# using while loop :
n = int(input("Enter a Number: "))
sum = 0      
i = 1
while(n>=i):
    sum = sum + i**3
    i = i+1
print(sum)

# using for loop :
n = int(input("Enter a Number: "))
sum = 0
for i in range(1,n+1):     
    sum += i**3
print(sum)