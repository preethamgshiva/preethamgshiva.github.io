s1=input("Enter a String: ")
l1=s1.split(" ")
count={}
for ch in l1:
    count.setdefault(ch,0)
    count[ch]=count[ch]+1
print(count)