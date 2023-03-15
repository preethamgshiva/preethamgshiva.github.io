import re
# case 1
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'^This')
for line in text:
    if kw.search(line):
        print(line)

#2
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw=re.compile('this', re.IGNORECASE)
for line in text:
    if kw.search(line):
        print(line)

#3
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'te')
for line in text:
    if kw.search(line):
        print(line)

#4
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'\bs\S*e\b')
for line in text:
    if kw.search(line):
        print(line)

#5
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'\d\d?\.\d\d?\.\d\d')
for line in text:
    if kw.search(line):
        print(line)