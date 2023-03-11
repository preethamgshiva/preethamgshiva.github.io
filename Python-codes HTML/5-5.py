it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

print(it_companies)

print(len(it_companies))

print(it_companies[0],it_companies[-1])

it_companies.append("samsung")
print(it_companies)

it_companies.insert(4,"Wipro")
print(it_companies)

it_companies[-1].upper()
print(it_companies)

for i in it_companies:
    i.join("#")
print(it_companies)