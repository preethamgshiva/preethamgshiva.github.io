s1=input("Enter a String: ")
a=s1[0]
for i in s1[1:]:
    s2=s1[1:].replace(a,"$")
print(a+s2)