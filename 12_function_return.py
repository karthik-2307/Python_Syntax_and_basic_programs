def sum(a,b):
    return float(a)+float(b)
def sub(a,b):
      return float(a)-float(b)
def mul(a,b):
      return float(a)*float(b)
def div(a,b):
      return float(a)/float(b)
def mod(a,b):
      return float(a)%float(b)
a=input("Enter the first number")
b=input("Enter the second number")
result=sum(a,b)
print("sum is :",result)
result=sub(a,b)
print("Diffrence is :",result)
result=mul(a,b)
print("Product is :",result)
result=div(a,b)
print("Division is :",result)
result=mod(a,b)
print("Modulus is :",result)
#Output would be
""""Enter the first number4
Enter the second number2
sum is : 6.0
Diffrence is : 2.0
Product is : 8.0
Division is : 2.0
Modulus is : 0.0"""