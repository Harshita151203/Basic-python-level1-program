# Check if a number is palindrome.

your_str = input("Enter Your String: ")

reverse_str = your_str[::-1]

if(your_str == reverse_str):
    print("Palindrome")
else:
    print("Not Palindrome")     