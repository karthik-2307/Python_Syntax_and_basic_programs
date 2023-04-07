#Printing the numbers one by one in an order of reverse order
num=int(input("Enter the number of points of the pyramid"))
for x in range(0,num+1):
    for y in range(num+1-x):
        print("*",end='')
    print()
'''Enter the number of points of the pyramid5
******
*****
****
***
**
*
'''