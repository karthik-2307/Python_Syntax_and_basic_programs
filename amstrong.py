temp=vari=num=int(input("Enter the input value"))
print("Input number is:",num)
count=0
while num>0:
    count=count+1
    # print(num)
    num=num//10
sum=0
print("Total number of digits in numbers is:",count)
while temp>0:
    sum=sum+pow((temp%10),count)
    temp=temp//10
print("sum of digits in terms of amstrong number is:",sum)
if sum==vari:
    print("Given number is an amstrong number")
else:
    print("Given number is not an amstrong number")