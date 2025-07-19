# Check if character is vowel or consonant.

user_choice = input("Enter your choice: ").lower()

mylist = ["a","e","i","o","u"]
if(user_choice in mylist):
    print("Vowels")
else:
    print("Consonent")