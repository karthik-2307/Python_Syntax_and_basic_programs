#Lets see about the power function using the loops
def pow(a,b):
    result=1
    for x in range(b):
         result=result*a
    return result
base=int(input("Enter the input for lower base"))
powe=int(input("Enter the power of the number")) 
print(pow(base,powe))
