import re
i=0
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    if re.search(r'(..).*\1',line) and re.search(r'(.).\1',line) :
        i+=1
print(i)
