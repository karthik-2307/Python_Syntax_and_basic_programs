#Finding the length of the list without the help of length function
list=[1,2,[],3,4,5,6,[],7,8,9,0,11,[]]
count=0
for x in list:
    count=count+1
print("The total length of the list is :",count)
#To clear elements of the list using clear funtion
print("Lists before clearing the empty lists:",list)
#Remove the empty lists from the lists
for x in list:
    if x==[]:
        list.remove(x)
print("List  after clearing empty lists is:",list)
print("List before clearing is:",list)
list.clear()
print("List after clearing is:",list)