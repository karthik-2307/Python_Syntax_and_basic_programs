#Here we would write into a file using python program
var=open("Hello.txt","w")
var.write(input("Enter the contents to the file"))
var.close()
print("Done with the statements")
var=open("Hello.txt","r")
print(var.read())
var.close()
#Writing function would help to write into the file and would erase the preveous content
'''Enter the contents to the fileKarthik
Done with the statements
Karthik'''