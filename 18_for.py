#For loop in python
#For sample range and printing table
num=int(input("Enter the number for which table is needed"))
for x in range(10):#From basic zer to last number
    print(x*num)
print("NEW LINE\n")
for x in range(1,11):#printing in given range
    print(x*num)
rollno=["A21126510001","A21126510002","A2112651027","A21126510024"]#Inialising the strings
for x in range(len(rollno)):#len function is used to find the length of the given array
    print("Student rollno is :"+rollno[x]) #Printing the array elements usig the index x where x can be the any integer 
print("Printing the corresponding odd numbers and even numbers in given range")
num1=int(input("Enter the starting number"))
num2=int(input("Enter the ending number"))
for x in range(num1,num2):#Printing in  the range of the given two numbers
    if x%2!=0:#Checking the condition of odd 
        print(x,"is odd number")
    else : #Checking the condition of even
        print(x,"is even number")
arr=[2,5,4,32,55]#Intializing the array with the elements off array
for x in range(len(arr)):
    if x%2!=0:
        print(arr[x])
    else :
        print(arr[x])
print("Ending of the loop")
