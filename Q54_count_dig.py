# Count digits in string.

string = input("Enter: ")
count = 0

for ch in string:
    if ch.isdigit(): 
        count += 1
print(f"Number of digits:{count}")       


