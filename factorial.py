#Finding the factorial through recurssion of a given number
def fact(n):
    print("Value of number is",n)
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the input to find the factorial"))
print("Factorial of the given number ",num,"is",fact(num))