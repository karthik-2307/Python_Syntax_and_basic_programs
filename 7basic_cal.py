#program for basic addition subraction and multiplication of the given two numbers
from math import *
num1=input("Enter the number 1 :")
num2=input("Enter the number 2 :")
#print("Sum is",int(num1)+int(num2))#Since if we enter a number of float it would represent an basic error...!
#So we would move for float data type
print("Sum is",float(num1)+float(num2))
print("Differernce is ",float(num1)-float(num2))
print("Multiplication is ",float(num1)*float(num2))
print("Division is ",float(num1)/float(num2))
print("Modulus would be ",float(num1)%float(num2))
print("Square root of num1 is :",sqrt(float(num1)))
print("Square root for num2 is:",sqrt(float(num2)))
print("roof of number 1 is:",ceil(float(num1)))
print("floor of num1 is :",floor(float(num1)))
print("roof of number 2 is:",ceil(float(num2)))
print("floor of num2 is :",floor(float(num2)))
print("Power of the given two a,b is",pow(float(num1),float(num2)))