x=0
y=0
grid_set={(x,y)}
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    for c in line:
        if c=='<':
            x=x-1
        elif c=='>':
            x=x+1
        elif c=='^':
            y=y+1
        elif c=='v':
            y=y-1
        grid_set.add((x,y))
print(len(grid_set))
