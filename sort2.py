num=int(input("Enter the size of list"))
list=[]
list1=[]
sort=[]
for x in range(0,num):
    ele=int(input("Enter the element st position at:"))
    list.append(ele)
    list1.append(ele)
print(list)
'''Desending order'''
while list:
    min=list[0]
    for x in list:
        if x>min:
            min=x
        
    sort.append(min)
    list.remove(min)
print(sort)
'''ascending order'''
sort=[]
while list1:
    min=list1[0]
    for x in list1:
        if x<min:
            min=x
    sort.append(min)
    list1.remove(min)
print(sort)