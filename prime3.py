num = int(input('Enter a number : '))
flag = 0
for i in range(2,num):
 if num%i == 0:
   flag = flag + 1

if flag==0:
 print('Its prime number')
else:
 print('Not Prime')