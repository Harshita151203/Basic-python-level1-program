# Remove all spaces from string.

string = input("Enter: ")      
no_space = ""

for ch in string:
    if ch !=" ":
     no_space +=ch 
print(no_space)          