# Check if number is prime.

n = int(input("Enter a Number: "))

if(n<=1):
    print("Not a Prime Number")
else:
    for i in range(2,n):
        if(n % i == 0):
            print("Not a Prime Number")
            break
    else:
         print("Prime Number") 

  
