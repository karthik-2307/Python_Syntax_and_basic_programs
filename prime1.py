#To verify whether a given number is a prime number or not
num=int(input("Enter the number to be checked"))
if num==1 or num==2 or num==3:
    print("IS prime")
elif num%2!=0 and num%3!=0:
    print("Is prime")
else:
    print("Not Prime")

