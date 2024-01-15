
flag=True
number=1357894
str_number=str(number)
lengthOfNumberDigits=len(str_number)
oddList=[1,3,5,7,9]
for i in oddList:
    if int(str_number[lengthOfNumberDigits-1])==i:   # [-1]
        flag=False
        break
if flag:
    print("even")
else:
    print("odd")
