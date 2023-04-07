#using functions without return statements
def add(a,b):
    print("Sum is :",float(a)+float(b))
def sub(a,b):
     print("Difference is :",float(a)-float(b))
def mul(a,b):
     print("Product is :",float(a)*float(b))
def div(a,b):
      print("Divison is :",float(a)/float(b))
def mod(a,b):
     print("Modulus is :",float(a)%float(b))
a=input("Enter the input of number 1")
b=input("Enter the input of number 2")
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
mod(a,b)
""""Enter the input of number 13
Enter the input of number 24
Sum is : 7.0
Difference is : -1.0
Product is : 12.0
Divison is : 0.75
Modulus is : 3.0"""