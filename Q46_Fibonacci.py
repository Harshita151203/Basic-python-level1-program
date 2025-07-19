# Program to print Fibonacci series using for loop

n = int(input("Enter a Number: "))
a = 0
b = 1
print("Fibonacci Series: ")

for i in range(n):
    print(a)
    a, b = b, a + b          