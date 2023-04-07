from classfile import hello#Importing the classfile into the current python file
name=input("Enter the name")
rollno=input("Enter the rollno")
section=input("Enter the section of student")
colleage=input("Enter the college name of student")
hello1=hello(name,rollno,section,colleage)#Creating the object to the class that was imported
print(hello1.name)#Accesing the details through object of the class
print(hello1.rollno)
print(hello1.section)
print(hello1.colleage)
'''Enter the nameKarthik
Enter the rollnoA21126510027
Enter the section of studentCSE-A
Enter the college name of studentANITS
Karthik
A21126510027
CSE-A
ANITS'''