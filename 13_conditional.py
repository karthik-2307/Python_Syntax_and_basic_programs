print("Starting of the program")
student=input("Enter the student if student True else False")
gender=input("Enter the Gender of student True if male else False")
if student and gender:
   print("Student and male")
elif student or gender:
   print("Student is male or female")
   print("In if statement")
if student or not(gender):
   print("HEllo student")
else :
   print("None of above")
print("Out of if statement")
""""Starting of the program
Enter the student if student True else FalseTrue
Enter the Gender of student True if male else FalseFalse
Student and male
Out of if statement"""