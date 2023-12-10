x=0
x2=0
y=0
y2=0
i=0
grid_set={(x,y)}
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    for c in line:
        if c=='<':
            if i%2==0:
                x=x-1
                grid_set.add((x,y))
            else:
                x2=x2-1
                grid_set.add((x2,y2))
        elif c=='>':
            if i%2==0:
                x=x+1
                grid_set.add((x,y))
            else:
                x2=x2+1
                grid_set.add((x2,y2))
        elif c=='^':
            if i%2==0:
                y=y+1
                grid_set.add((x,y))
            else:
                y2=y2+1
                grid_set.add((x2,y2))
        elif c=='v':
            if i%2==0:
                y=y-1
                grid_set.add((x,y))
            else:
                y2=y2-1
                grid_set.add((x2,y2))
        i+=1
print(len(grid_set))
