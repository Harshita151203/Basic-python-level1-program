#  Find largest among three numbers.

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))


if(num1>num2 and num1>num3):
 print(f"Greatest Number is {num1}")
elif(num2>num1 and num2>num3):
 print(f"Greatest Number is {num2}")
else:
 print(f"Greatest Number is {num3}")
