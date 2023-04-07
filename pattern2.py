#Printing the numbers one by one in an order
num=int(input("Enter the number of points of the pyramid"))
for x in range(0,num+1):
    for y in range(x):
        print(y+1,end='')
    print()
'''Enter the number of points of the pyramid8

1
12
123
1234
12345
123456
1234567
12345678
'''