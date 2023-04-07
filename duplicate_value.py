list=[]
num=int(input("Enter the size of the list"))
for i in range(0,num):
    list.append(int(input("Enter the input")))
mul=[]
dup=[]
for x in list:
    if x not in mul:
        mul.append(x)
    elif x not in dup: 
        dup.append(x)
print("Multiple values are:",mul)
print("Duplicate values are:",dup)