def longest():
    s1=input("Enter a String: ")
    l1=s1.split(" ")
    l1.sort(key=len)
    print(l1[-1])
longest()