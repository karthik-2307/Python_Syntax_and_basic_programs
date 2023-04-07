string1=input("enter the string value")
num=len(string1.split(' '))#Splits to the number of words
tot=len(string1)
print("Total length:",tot)
print("the number of characters is:",abs(tot-num))
print(num)