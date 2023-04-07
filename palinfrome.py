var=input("enter the string to be checked")
rever=var[::-1]
if var==rever:
    print("Given string is palindrome")
else:
    print("Given string is not a palindrome")
#Without indexing 
print("Without indexing")
back=""
for x in var:
   back=x+back
print("Reversed value of input is:"+back)
if back==var:
    print("Given one is a palindrome")
else :
    print("Given string is not a palindrome")