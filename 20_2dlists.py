#Lists are basically similar to arrays as we have seen the lists in previous programs now we would see about two dimensioal lists
list=[
    [1,2,3,4],
    [4,3,2,1],
    [5,6,7,8],
    [8,7,6,5],
    [0]
]
#We can access these elements through the print statement directly
print(list)
#Output is in this kind
#PS C:\Users\Y.KARTHICK REDDY\Desktop\python> & "C:/Users/Y.KARTHICK REDDY/AppData/Local/Programs/Python/Python311/python.exe" "c:/Users/Y.KARTHICK REDDY/Desktop/python/20_2dlists.py"
#[[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8], [8, 7, 6, 5], [0]]
#PS C:\Users\Y.KARTHICK REDDY\Desktop\python> """
#we can also see how to access each elements individually through for loops
for x in list:
    print(x)#prints the each row seprately 
"""[1, 2, 3, 4]
[4, 3, 2, 1]
[5, 6, 7, 8]
[8, 7, 6, 5]
[0]"""
for x in list:
    for y in x:
        print(y)#Prints every element seprately and individually
"""1
2
3
4
4
3
2
1
5
6
7
8
8
7
6
5
0"""