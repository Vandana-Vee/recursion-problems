# st = "abcde"
# set = [""]
# l = 5
# for i in range(l):
#     set.append(st[i])
# for a in range(l-1):
#     temp=st[a]
#     temp2=str(temp)
#     for b in range(a+1,l):
#         temp2+=st[b]
#         set.append(temp2)

# print(set)


st = "abcde"
set = [""]
l = 5
for i in range(l):
    set.append(st[i])
for a in range(l-1):
    temp=st[a]
    temp2=str(temp)
    for b in range(a+1,l):
        temp2=st[b]
        temp3=temp+temp2
        set.append(temp3)

print(set)