# Check if string is palindrome..

string = input("Enter Your String: ")
rev = string[::-1]

if(string == rev):
    print("Palindrome")
else:
    print("Not Palindrome")    