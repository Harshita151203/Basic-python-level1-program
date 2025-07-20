# Replace all vowels with * in string.

string = input("Enter Your String: ")
vow = "aeiouAEIOU"
new = ""

for ch in string:
    if ch in vow:
        new += "*"
    else:
        new += ch

print(new)