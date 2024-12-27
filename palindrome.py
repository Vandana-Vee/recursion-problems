
def pal(str,si,ei):
    if si==ei or si>ei:
        return True
    
    if(str[si]==str[ei]):
        return pal(str,si+1,ei-1)
    else:
        return False

def caller(str):
    ei = len(str)-1
    return pal(str,0,ei)

str = input("Enter string to check for palindrome: ")
print(caller(str))