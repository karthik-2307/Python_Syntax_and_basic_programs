#We would see the method of reading and appending into a file
var=open("Hello.txt","r")
print(var.read())#Reads the entire content of the file
print("Checking permission for readable: ",var.readable())
'''Karthik
Komal
Balu
Easwer
Rahul
Bobby
Checking permission for readable:  True'''
var.close()
var=open("Hello.txt","r")
print(var.readline())#Reads the first line of the file
for x in var.readlines():#Used to print entire lines of the file
    print(x)
var.close()
var=open("Hello.txt","a")#Appends the string to the file
var.write("\nHello")
var.close()