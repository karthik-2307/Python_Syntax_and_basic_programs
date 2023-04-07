lists=[2,2,2,2,431,241,245,522,998907]
dec=[]
print(lists)
sorted(lists)
num=len(lists)
print(num)
for x in range(0,num):
    #print(lists[x-num])
    dec.append(lists[x-num])
print(lists[-2])
'''For removing the duplicate elements from lists'''
list2=list(set(lists))
print(dec)
print(list2)