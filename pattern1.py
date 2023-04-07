#draw a right angles triange using the patterns
num=int(input("Enter the number of points of the pyramid"))
for x in range(0,num+1):
    for y in range(x):
        print("*",end='')
    print()
    '''*
**
***
****
*****
******
'''