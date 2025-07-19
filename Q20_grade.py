# Assign grade (A/B/C/Fail) based on marks.

user_marks = int(input("Enter Your Marks: "))  

if(user_marks <= 0 or user_marks > 100):
    print("Invalid Marks Enter!")
elif(user_marks >= 90 and user_marks <= 100):
    print("A+")
elif(user_marks >= 80 and user_marks <= 89):  
    print("A")
elif(user_marks >= 70 and user_marks <= 79):
    print("B")
elif(user_marks >= 60 and user_marks <= 69 ):
    print("C")
elif(user_marks >= 50 and user_marks <= 59):
    print("D")
elif(user_marks >= 35 and user_marks <= 49):
    print("E")  
elif(user_marks < 35):
    print("FAIL")
