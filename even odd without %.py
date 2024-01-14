
flag=True
number=2375
str_number=str(number)
ones=len(str_number)
oddList=[1,3,5,7,9]
for i in oddList:
    if int(str_number[ones-1])==i:
        flag=False
if flag:
    print("even")
else:
    print("odd")
    