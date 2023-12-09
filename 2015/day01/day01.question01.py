line_sum=0
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    floors_up=line.count('(')
    floors_down=line.count(')')
    final_floor=floors_up-floors_down
    print(final_floor)
