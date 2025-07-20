# Count vowels in string.

abc = "aeiouAEIOU"
string = input("Enter: ")
count = 0

for ch in string:
 if ch in abc:
    count += 1
print(f"Number of Vowels: {count}")

    
