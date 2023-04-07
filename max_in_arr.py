n=int(input("Enter the size of list"))
list=[]
for i in range(0,n):
    list.append(int(input("Enter the input variable")))
print(list)
max=list[0]
for i in list:
    if max<i:
        max=i
print("Maximum value among the list is:",max)
'''stl function for sorting is sorted(list_name)'''
print(sorted(list))
print(sorted(list,reverse=True))#In decending order
