st = "babe"
print(st[::-1])

def rev(st,l):
    if l==(len(st)-1):
        return 
    rev(st,l+1)

rev(st,0)