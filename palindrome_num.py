num=num1=int(input("Enter the number to be checked to verify the palindrome"))
pal=0
#print(5//2)#If single slash is used it results the points value too so we use '//' so that we can get qutiont
while (num>0):
    pal=pal*10+num%10
    num=num//10
print("Reversed value is:",pal)
print("Orginal value is:",num1)
if num1==pal:
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")