student=["Karthik","Rahul","Sai",True,False,'A',2307]#Basically list is simply used to store anykind of data in a single name and would give acces through the indexes
id=[23,43,2]
print(student)#prints the entire list of the elements
print(student[0])#prints the elemets given in the current index
print(student[0:])#prints the elements from the index given to the ending index
print(student[0:2])#prints the elements in the given range
print(student[-7])
print(student[-6])
print(student[-1])#Prints the elemnts with the negetive index starting from the end
student[0]="Ashok"#Used to change the string that is present in the given index...!
print(student[0])
#Lets see some of the functions in the lists
student=["Karthik","Rahul","Sai",True,False,'A',2307]
id=[23,43,2]
id.sort()#sorts the given list 
print(id)
print(student.count(2307))#Counts the number of elements present in list as per given input
student.reverse()#prints all the elements in the reverse order
print(student)
print(student.pop())#Removes the last elements from the list
student.insert(2,"Balu")#Inserts the given element into the given list
print("Inserted balu ",student)
student.remove(2307)#Removes the given element from the list suppose if element is not present it would give an error message
print(student)
student.extend("8")#It would add the given element to the last position of the list
print(student)
student.extend(id)#It would extend the given source list to the destination list
print(student)
friends=student.copy()
print(friends)#Copies the given list to the destination list
print(friends.index("Sai"))
print(student.clear())#Clears the entire list
#OUTPUT IS
"""['Karthik', 'Rahul', 'Sai', True, False, 'A', 2307]
Karthik
['Karthik', 'Rahul', 'Sai', True, False, 'A', 2307]
['Karthik', 'Rahul']
Karthik
Rahul
2307
Ashok
[2, 23, 43]
1
[2307, 'A', False, True, 'Sai', 'Rahul', 'Karthik']
Karthik
Inserted balu  [2307, 'A', 'Balu', False, True, 'Sai', 'Rahul']
['A', 'Balu', False, True, 'Sai', 'Rahul']
['A', 'Balu', False, True, 'Sai', 'Rahul', '8']
['A', 'Balu', False, True, 'Sai', 'Rahul', '8', 2, 23, 43]
['A', 'Balu', False, True, 'Sai', 'Rahul', '8', 2, 23, 43]
4
None"""