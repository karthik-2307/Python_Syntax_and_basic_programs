# Very important suppose we are saving some number with varaible and that variable
# is assign to some new variable so if you make changes in old variable no change will happ
# in newly assign variable because string and integer are immutable
num=int(input("Enter the input: "))
temp=num
print("Orginal number is:",num)
print("Copied number is :",temp)
print("Adress of orginal value is:",id(num))
print("Adress of copied value is:",id(temp))
num=num+1
print("Orginal value is:",num)
print("Copied value is :",temp)
print("Adress of orginal value:",id(num))
print("Adress of copied value :",id(temp))
#As we had observed the output of the given variable is changed...!
'''Enter the input: 23
Orginal number is: 23
Copied number is : 23
Adress of orginal value is: 140731410478568
Adress of copied value is: 140731410478568
Orginal value is: 24
Copied value is : 23
Adress of orginal value: 140731410478600
Adress of copied value : 140731410478568'''