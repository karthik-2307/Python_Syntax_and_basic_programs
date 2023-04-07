#Finding the factorial of the given number through the for loops
num=int(input("Enter the number to find the factorial"))
res=1
if num==1 or 0:
    print("Factorial of the given number is :",1)
else:
    for x in range(2,num+1):
       res=res*x
    print("Factorial of the given number is:",res)