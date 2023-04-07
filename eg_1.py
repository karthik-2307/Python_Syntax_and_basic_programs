#To check whether a number is present in list or not
list=[]
num=int(input("Enter the size of the list:"))
for x in range(0,num):
    list.append(int(input("Enter the input to the list")))

var=int(input("Enter the number to be checked in the list"))
count=0
for x in list:
    if x==var:
        print("Number is found in the list")
        count=count+1
        break
if count==0:
    print("Number not found in the list")