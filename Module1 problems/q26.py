num = str(input("Number: "))

if len(num)==1:
    print("1 digit")
if len(num)==2:
    print("2 digits")
if len(num)==3:
    print("3 digits")
elif len(num)>3:
    print("More than 3 digits")