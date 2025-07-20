# Check if a number is palindrome.

your_num = input("Enter Your Number: ")


if(your_num == your_num[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")     
