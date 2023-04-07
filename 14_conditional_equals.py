#Here we were used to compare between the two values or strings etc....!
num1=input("Enter the input for number 1 :")
num2=input("Enter the input for number 2 :")
if num1>num2:
    print("Number 1 is larger")
elif num2>num1:
    print("Number 2 is larger")
elif num1==num2:
    print("Both the numbers are equal")
#Now we would check about strings||Similarly it would also compares the given characters and float values
str1=input("Enter string 1")
str2=input("Enter string 2")
if str1==str2 :
    print("Both the strings are equal")
elif str1>str2:
    print("String 1 is greater than string 2")
elif str2>str1:
    print("String 2 is greater than String 1")
else :
    print("Both the given strings are not equal")
"""Enter the input for number 1 :34
Enter the input for number 2 :43
Number 2 is larger
Enter string 1Karthik
Enter string 2karthik
String 2 is greater than String 1"""