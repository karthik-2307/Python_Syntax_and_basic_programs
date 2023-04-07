#Creating the star pyramid using stars
num=int(input("Enter the count of the stars"))
k=0
for x in range(1,num+1):
     for space in range(1,(num-x)+1):
         print(end=" ")
     while k!=(2*x-1):
         print("*",end="")
         k=k+1

     k=0
     print()
'''Enter the count of the stars5
    *
   ***
  *****
 *******
*********
'''