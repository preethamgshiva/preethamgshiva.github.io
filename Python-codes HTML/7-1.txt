str1=str(input("Enter a string: "))
count={}
for ch in str1:
    count.setdefault(ch,0)
    count[ch]=count[ch]+1
print(count)