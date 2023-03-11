#use of break and continue statement

n = int(input("Range: "))
for i in range(n+1):
    if i==5:
    
        break
    print(i)

for i in range(n+1):
    if i==6:
        continue
    print(i)