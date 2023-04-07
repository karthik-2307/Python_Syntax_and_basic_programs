#Printing the numbers one by one in an reverse order
num=int(input("Enter the number of points of the pyramid"))
for x in range(0,num+1):
    for y in range(num+1-x):
        print(y+1,end='')
    print()
'''Enter the number of points of the pyramid5
123456
12345
1234
123
12
1
'''