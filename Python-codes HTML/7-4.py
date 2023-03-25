s1=input("Enter a String: ")
if s1.endswith("ing")==True:
    s2=s1.replace("ing","ly")
    print(s2)
else:
    print(s1+"ing")