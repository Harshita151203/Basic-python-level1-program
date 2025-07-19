#Print multiplication table for a number up to 10.

num = int(input("Enter any number: "))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")