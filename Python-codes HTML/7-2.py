str2=input("Enter a string: ")
a=str2[0:2]
b=str2[len(str2)-2:]
print(a+b)
if len(str2)<2:
    print(str2)