dist=float(input("Enter the total distace travelled in kilometers: "))
amt_fuel=float(input("Enter the amount per litre of fuel: "))
milage=int(input("Enter milage of the vehicle: "))

total_ppl=6

total_fuel=dist/milage
total_amount=total_fuel*amt_fuel
amt_divided=total_amount/6

print("Amount shared by each people is ",amt_divided)

if amt_divided%3==0:
    print("True")
else:
    print("False")