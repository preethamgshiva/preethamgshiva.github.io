ages = [19,22,19,24,20,25,26,24,25,24]

ages.sort()
#to Print min and max value
print(ages[0],ages[-1])

#to add min and max value
print(ages[0]+ages[-1])

#to find median
median=len(ages)//2
print(ages[median+1])

#average sum
sum=0
for i in ages:
    sum=sum+i
    avg=sum/len(ages)
print(avg)

#range of the ages
print(ages[-1]-ages[0])