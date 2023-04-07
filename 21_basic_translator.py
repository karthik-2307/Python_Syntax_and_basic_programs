#here we would see the translator ie..) we would convert the vovels present in the given string to any character as per our wish
def convert(orginal,ch):
    final=""
    for x in orginal:
        if x.upper() in "AEIOUaeiou":#Here we would check the character if it is present in the vovels or not
            final=final+ch#Appending the character to the final string if it is vovel we would change them
        else :
            final=final+x#we would append the statement with the non vivel character
    return final#Returning the final statement 
orginal=input("Enter the orginal string")
character=input("Enter the character that is needed to change")
print(convert(orginal,character))#Calling the function for checking
#Comments can be done through the ''' data '''