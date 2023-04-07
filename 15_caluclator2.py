#here we would write a program using the basic if and else if statements 
num1=float(input("Enter the number1 :"))
num2=float(input("Enter the number2 :"))
operator=input("Enter the input operator")
if operator=="+":
    print("Sum is :",num1+num2)
elif operator=="-":
    print("Difference is :",num1-num2)
elif operator=="*":
    print("Product is :",num1*num2)
elif operator=="/":
    print("Division is :",num1/num2)
elif operator=="%":
    print("Modulus is :",num1%num2)
else :
    print("invalid operator")
""""Enter the number1 :23
Enter the number2 :32
Enter the input operator*
Product is : 736.0"""