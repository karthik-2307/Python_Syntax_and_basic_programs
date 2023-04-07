#Counts the total number of letters....!
val=input("Enter the string input")
dic={}
for x in val:
    if x in dic:
        dic[x]=dic[x]+1
    else:
        dic[x]=1
print(dic)
dic1={'key':'a','value':0}
for x in dic:
    if dic1['value']<dic[x]:
        dic1['key']=x
        dic1['value']=dic[x]
print(dic1)