#  Count consonants in string.

string = input("Enter: ")  
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch.isalpha() and ch not in vowels:
        count = count +1
print(f"Number of Consonants: {count}")