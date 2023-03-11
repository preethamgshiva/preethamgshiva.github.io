# multiplication-table of a number

num=int(input("Enter a number: "))
_range=int(input("Enter range: "))

for i in range(_range+1):
    print(num,"*",i,"=",i*num)