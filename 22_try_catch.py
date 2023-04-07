'''Try catch exception error handling these are use to handle the errors that are arised in the program and we would handle this error
Syntax:try :
           //statements//
           in which the errors may arise
        except:
            except is used to handle the exception
            we can write the exception followed by as and error name so that we were able to find the name of error'''
#lets see some examples for division of two numbers...!
try:
    num1=int(input("Enter the input of 1st number"))
    num2=int(input("enter the input of 2nd number"))
    string=float(input("Enter the numerial input"))
    print(num1/num2)
except ValueError as err:
    print("Value error")
    print(err)
except ZeroDivisionError as var:#used to identify the zero division error
    print("INVALID ERROR ARISED")
    print(var)
'''Enter the input of 1st number10
enter the input of 2nd number0
INVALID ERROR ARISED
Enter the input of 1st numberstr
Value error
invalid literal for int() with base 10: str
Enter the input of 1st number3
enter the input of 2nd number4
Enter the numerial inputsda
Value error
could not convert string to float: 'sda'''
#Similarly we are having multiple errors but we can handle all of them through the single statement known as except