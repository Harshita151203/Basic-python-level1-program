# Check if character is uppercase or lowercase.

user_choice = input("Enter Your String: ")


if(user_choice.isupper()):
        print("Upper")
elif(user_choice.islower()):
        print("Lower")
else:
        print("Mix String")