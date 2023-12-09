line_sum=0
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    print(line)
    num = ""
    for c in line:
       if c.isdigit():
          num = num + c

    line_num=num[0]+num[-1]
    print(int(line_num))
    line_sum=line_sum+int(line_num)
print(line_sum)
