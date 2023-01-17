principle = float(input("Principle: "))
time = float(input("Time in years: "))

if time>8:
     intrest = 12

else:
     intrest = 18

SI = (principle*time*intrest)/100

print("Your simple intrest is ", SI)