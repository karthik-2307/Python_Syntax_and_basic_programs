num=int(input("Enter the size of list"))
list=[]
sort=[]
for x in range(0,num):
    list.append(int(input("Enter the element st position at:")))
print(list)
min=100000
for x in range(0,num):
    for y in range(x+1,num):
        if list[x]>list[y]:
            list[x],list[y]=list[y],list[x]
  #  sort.append(min)
print(list)