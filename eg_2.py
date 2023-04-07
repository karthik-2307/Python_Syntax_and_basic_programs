#Extraction digits from the given string
num=input("Enter the input of type string")
digits=''
for x in num:
    if x.isdigit()==True:
        digits=digits+x

print(digits)
