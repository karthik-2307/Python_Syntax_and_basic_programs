num=int(input("Enter the size of list"))
list=[]
sort=[]
for x in range(0,num):
    list.append(int(input("Enter the element st position at:")))
print(list)
#sorted(list)
'''
for x in range(0,len(list)-1):
    prev=list[x]
    print(prev)
    next=list[x+1]
    try:
         if prev==next:
         # list.remove(prev)
          sort.append(prev)
        #  x=x-1
    except:
        print()
        '''
for x in list:
    if x not in sort:
        sort.append(x)
print(list)
print(sort)