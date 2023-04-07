def fib(a):
  #  print(a)
    if a==0:
        print('invalid input')
        return 0
    elif a==1 or a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)
print('Fibbonaci sequence')
num1=int(input("Enter the range of number up to where you want to print"))
print("Respected sequence is:")
for i in range(0,num1):
  print(fib(i))
print("Sequence has ended")