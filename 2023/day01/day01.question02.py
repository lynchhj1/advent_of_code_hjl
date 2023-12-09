import re

line_sum=0
replacements = [
    ('one','o1e'),
    ('two','t2o'),
    ('three','t3e'),
    ('four','f4r'),
    ('five','f5e'),
    ('six','s6x'),
    ('seven','s7n'),
    ('eight','e8t'),
    ('nine','n9e')
]

file = open('input', 'r')
lines = file.readlines()
for line in lines:
    print(line)
    for old, new in replacements:
      line = re.sub(old, new, line)
    print(line)
    num = ""
    for c in line:
       if c.isdigit():
          num = num + c

    line_num=num[0]+num[-1]
    print(int(line_num))
    line_sum=line_sum+int(line_num)
print(line_sum)
