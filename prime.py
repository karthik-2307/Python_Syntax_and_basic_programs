num1=int(input("Enter the number 1"))
num2=int(input("Enter the number 2"))
for x in range(num1,num2):
    if x==2 or x==3 and x!=1:
        print(x)
    elif x%2!=0 and x%3!=0 and x!=1:
        print(x)